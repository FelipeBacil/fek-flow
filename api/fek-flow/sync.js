const { neon } = require("@neondatabase/serverless");
const { randomUUID } = require("crypto");

function getConnectionString() {
  return (
    process.env.DATABASE_URL ||
    process.env.POSTGRES_URL ||
    process.env.POSTGRES_PRISMA_URL ||
    process.env.NEON_DATABASE_URL ||
    ""
  );
}

function emptyState() {
  return { projects: [], activeProjectId: null };
}

function normalizeState(value) {
  if (!value || typeof value !== "object") return emptyState();
  return {
    projects: Array.isArray(value.projects) ? value.projects : [],
    activeProjectId: value.activeProjectId || null,
  };
}

function addRecord(project, event, owner) {
  project.records = Array.isArray(project.records) ? project.records : [];
  project.records.push({
    date: new Date().toISOString(),
    event,
    owner: owner || "Sistema",
  });
}

function nextProjectCode(projects) {
  let max = 0;
  projects.forEach((project) => {
    const match = String(project.code || "").match(/(\d+)$/);
    if (match) max = Math.max(max, Number(match[1]));
  });
  return `PRJ-${String(max + 1).padStart(3, "0")}`;
}

function applyAction(state, type, payload) {
  const projects = state.projects;

  if (type === "create_project") {
    const project = { ...(payload.project || {}) };
    project.id = project.id || randomUUID();
    project.code = project.code || nextProjectCode(projects);
    project.tasks = project.tasks && typeof project.tasks === "object" ? project.tasks : {};
    project.records = Array.isArray(project.records) ? project.records : [];
    project.createdAt = project.createdAt || new Date().toISOString();
    addRecord(project, "Projeto criado", project.owner || "Sistema");
    projects.push(project);
    state.activeProjectId = project.id;
    return { projectId: project.id };
  }

  if (type === "delete_project") {
    const index = projects.findIndex((project) => project.id === payload.projectId);
    if (index < 0) throw new Error("Projeto não encontrado.");
    projects.splice(index, 1);
    if (state.activeProjectId === payload.projectId) state.activeProjectId = null;
    return {};
  }

  if (type === "update_task") {
    const project = projects.find((item) => item.id === payload.projectId);
    if (!project) throw new Error("Projeto não encontrado.");
    project.tasks = project.tasks && typeof project.tasks === "object" ? project.tasks : {};
    const task = project.tasks[payload.taskKey];
    if (!task) throw new Error("Atividade não encontrada.");
    Object.assign(task, payload.changes || {});
    addRecord(project, `Atividade atualizada: ${task.title || payload.taskKey}`, task.owner || "Sistema");
    return {};
  }

  if (type === "create_activity") {
    const project = projects.find((item) => item.id === payload.projectId);
    if (!project) throw new Error("Projeto não encontrado.");
    project.tasks = project.tasks && typeof project.tasks === "object" ? project.tasks : {};
    const activity = { ...(payload.activity || {}) };
    const key = `custom|${Date.now()}|${Math.random().toString(36).slice(2, 8)}`;
    project.tasks[key] = {
      title: activity.title || "Nova atividade",
      stage: activity.stage || "Atividades adicionais",
      discipline: activity.discipline || "Atividade avulsa",
      owner: activity.owner || "",
      deadline: activity.deadline || "",
      priority: activity.priority || "Normal",
      status: activity.status || "Pendente",
      description: activity.description || "",
    };
    addRecord(project, `Atividade criada: ${project.tasks[key].title}`, project.tasks[key].owner || "Sistema");
    return { taskKey: key };
  }

  throw new Error(`Ação não suportada: ${type || "não informada"}.`);
}

module.exports = async function handler(req, res) {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");

  try {
    const connectionString = getConnectionString();
    if (!connectionString) {
      return res.status(500).json({ error: "Banco Neon não configurado no ambiente do Vercel." });
    }

    const sql = neon(connectionString);

    await sql`
      CREATE TABLE IF NOT EXISTS fek_flow_state (
        id INTEGER PRIMARY KEY,
        revision BIGINT NOT NULL DEFAULT 0,
        state JSONB NOT NULL,
        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
      )
    `;

    await sql`
      INSERT INTO fek_flow_state (id, revision, state)
      VALUES (1, 0, ${JSON.stringify(emptyState())}::jsonb)
      ON CONFLICT (id) DO NOTHING
    `;

    const rows = await sql`SELECT revision, state FROM fek_flow_state WHERE id = 1`;
    const current = rows[0] || { revision: 0, state: emptyState() };
    const state = normalizeState(current.state);
    const revision = Number(current.revision || 0);

    if (req.method === "GET") {
      return res.status(200).json({ revision, state });
    }

    if (req.method !== "POST") {
      res.setHeader("Allow", "GET, POST");
      return res.status(405).json({ error: "Método não permitido." });
    }

    const body = req.body && typeof req.body === "object" ? req.body : {};
    const result = applyAction(state, body.type, body.payload || {});
    const nextRevision = revision + 1;

    await sql`
      UPDATE fek_flow_state
      SET revision = ${nextRevision},
          state = ${JSON.stringify(state)}::jsonb,
          updated_at = NOW()
      WHERE id = 1
    `;

    return res.status(200).json({ revision: nextRevision, state, ...result });
  } catch (error) {
    console.error("FEK Flow sync error:", error);
    return res.status(500).json({ error: error.message || "Erro interno de sincronização." });
  }
};
