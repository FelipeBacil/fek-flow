from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


FEK_DIRECTORIES = [
    "docs",
    "docs/architecture",
    "docs/decisions",
    "management",
    "management/activities",
    "management/exports",
    "specs",
    "tests",
    "examples",
    "data/materials",
    "data/sections",
    "data/validation",
    "tools",
    "src/core",
    "src/geometry_engine",
    "src/topology_engine",
    "src/engineering_model",
    "src/material_engine",
    "src/load_engine",
    "src/mesh_engine",
    "src/simulation_engine",
    "src/visualization_engine",
    "src/report_engine",
    "src/solver_interface",
]

MODULES = [
    "core",
    "geometry_engine",
    "topology_engine",
    "engineering_model",
    "material_engine",
    "load_engine",
    "mesh_engine",
    "simulation_engine",
    "visualization_engine",
    "report_engine",
    "solver_interface",
]


def write_if_missing(path: Path, content: str) -> bool:
    """Create a text file only when it does not already exist."""
    if path.exists():
        return False

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def build_activity_index() -> dict:
    now = datetime.now(timezone.utc).isoformat()

    return {
        "schema_version": "1.0.0",
        "project": {
            "id": "FEK",
            "name": "Fengbir Engineering Kernel",
            "status": "active",
        },
        "generated_at": now,
        "dashboard": {
            "source": "FEK",
            "export_file": "management/exports/fek-dashboard.json",
            "consumer": "Fengbir Site",
        },
        "modules": [
            {
                "id": module,
                "name": module.replace("_", " ").title(),
                "status": "planned",
                "progress": 0,
                "activities": [],
            }
            for module in MODULES
        ],
    }


def build_dashboard_export(activity_index: dict) -> dict:
    return {
        "schema_version": activity_index["schema_version"],
        "generated_at": activity_index["generated_at"],
        "project": activity_index["project"],
        "summary": {
            "modules_total": len(activity_index["modules"]),
            "modules_planned": len(activity_index["modules"]),
            "modules_in_progress": 0,
            "modules_completed": 0,
            "overall_progress": 0,
        },
        "modules": activity_index["modules"],
    }


def main() -> None:
    root = Path(__file__).resolve().parent

    print(f"FEK Bootstrap")
    print(f"Root: {root}")
    print("-" * 60)

    for relative_path in FEK_DIRECTORIES:
        directory = root / relative_path
        directory.mkdir(parents=True, exist_ok=True)
        print(f"[DIR] {relative_path}")

    created_files: list[str] = []

    readme = """# FEK — Fengbir Engineering Kernel

Kernel de engenharia especializado em implementos rodoviários, estruturas
soldadas, automação CAD/CAE e preparação de modelos para simulação.

## Princípio arquitetural

O FEK permanece desacoplado do site Fengbir. O site consome somente dados
publicados pelo FEK por meio de arquivos de exportação versionados.

## Integração inicial com o site

Fonte oficial:

`management/activity-index.json`

Arquivo de consumo do dashboard:

`management/exports/fek-dashboard.json`
"""
    if write_if_missing(root / "README.md", readme):
        created_files.append("README.md")

    gitkeep_paths = [
        "docs/architecture/.gitkeep",
        "docs/decisions/.gitkeep",
        "management/activities/.gitkeep",
        "specs/.gitkeep",
        "tests/.gitkeep",
        "examples/.gitkeep",
        "data/materials/.gitkeep",
        "data/sections/.gitkeep",
        "data/validation/.gitkeep",
        "tools/.gitkeep",
    ]

    for relative_path in gitkeep_paths:
        if write_if_missing(root / relative_path, ""):
            created_files.append(relative_path)

    for module in MODULES:
        module_readme = f"""# {module.replace("_", " ").title()}

## Responsabilidade

Definição pendente na especificação FES correspondente.

## Estado

Planned.
"""
        relative_path = f"src/{module}/README.md"
        if write_if_missing(root / relative_path, module_readme):
            created_files.append(relative_path)

    activity_index_path = root / "management/activity-index.json"
    if not activity_index_path.exists():
        activity_index = build_activity_index()
        activity_index_path.write_text(
            json.dumps(activity_index, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        created_files.append("management/activity-index.json")
    else:
        activity_index = json.loads(activity_index_path.read_text(encoding="utf-8"))

    dashboard_path = root / "management/exports/fek-dashboard.json"
    if not dashboard_path.exists():
        dashboard = build_dashboard_export(activity_index)
        dashboard_path.write_text(
            json.dumps(dashboard, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        created_files.append("management/exports/fek-dashboard.json")

    print("-" * 60)
    if created_files:
        print("Files created:")
        for item in created_files:
            print(f"[FILE] {item}")
    else:
        print("No files needed to be created.")

    print("-" * 60)
    print("Bootstrap completed without moving or deleting existing files.")
    print("Next validation: inspect the generated folder tree and JSON files.")


if __name__ == "__main__":
    main()
