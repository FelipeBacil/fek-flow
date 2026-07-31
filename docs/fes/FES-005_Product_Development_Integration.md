# FES-005 — Integração do Desenvolvimento de Produto ao FEK Flow

**Código:** FES-005  
**Título:** Integração do FEK Product Flow ao FEK Flow  
**Revisão:** R00  
**Data:** 31/07/2026  
**Status:** Arquitetura definida — implementação ainda não iniciada  
**Aplicação:** FEK Flow / Workspace de Projetos  

---

## 1. Objetivo

Definir a arquitetura de integração do FEK Product Flow ao FEK Flow, eliminando a duplicidade existente na etapa **3. Detalhamento Multidisciplinar** e estabelecendo uma única fonte de verdade para o desenvolvimento técnico de produtos.

A integração deve preservar:

- a governança corporativa do FEK Flow;
- a lógica técnica validada no FEK Product Flow;
- o histórico dos projetos já existentes;
- a rastreabilidade entre atividade, evidência, decisão, gate e documento;
- o desacoplamento entre interface, regras de workflow e motores de engenharia.

## 2. Problema identificado

O FEK Flow atualmente contém, dentro da etapa **3. Detalhamento Multidisciplinar**, atividades técnicas detalhadas de estrutura, caixa de carga, montagem e sistemas.

O FEK Product Flow foi desenvolvido posteriormente para tratar exatamente esse domínio, porém com maior profundidade, automação condicional, gates técnicos, fornecedores, CAE, protótipo, requisitos e databook.

A manutenção das duas estruturas em paralelo causa:

- duplicidade de atividades;
- divergência entre status;
- repetição de evidências;
- incerteza sobre o sistema proprietário de cada informação;
- risco de evolução inconsistente;
- aumento de manutenção;
- experiência operacional excessivamente burocrática.

## 3. Decisão arquitetural

O FEK Product Flow deixa de ser tratado como aplicação independente de destino final e passa a constituir o módulo especializado:

> **FEK Flow — Desenvolvimento de Produto**

O FEK Flow permanece como aplicação principal e proprietário de:

- portfólio de projetos;
- usuários e permissões;
- processo corporativo;
- etapas macro;
- responsáveis setoriais;
- registros e histórico;
- aprovações corporativas;
- integração entre áreas;
- encerramento do projeto.

O módulo Desenvolvimento de Produto passa a ser proprietário de:

- requisitos técnicos do produto;
- pré-dimensionamento estrutural;
- arquitetura do produto;
- longarina;
- chassi;
- caixa de carga;
- sistemas e acessórios;
- rodagem;
- fornecedores técnicos;
- CAE;
- protótipo técnico;
- gates técnicos;
- evidências de engenharia;
- índice do databook técnico.

## 4. Princípio de responsabilidade

Cada informação deve possuir um único sistema proprietário.

| Informação | Sistema proprietário |
|---|---|
| Projeto, cliente, prioridade e prazo corporativo | FEK Flow |
| Processo e etapa macro | FEK Flow |
| Requisitos técnicos do produto | Desenvolvimento de Produto |
| Atividades detalhadas de engenharia | Desenvolvimento de Produto |
| Cálculos e simulações computacionais | FEK Kernel |
| Evidências e resultados técnicos | Desenvolvimento de Produto |
| Aprovação multidisciplinar corporativa | FEK Flow |
| Modelos CAD e desenhos oficiais | PDM |
| Itens, BOM e dados produtivos | ERP/PDM |
| Conhecimento, decisões e lições aprendidas | Confluence / Databook |

## 5. Estrutura macro resultante

```text
FEK Flow
├── 1. Solicitação de Desenvolvimento
├── 2. Análise Crítica
├── 3. Desenvolvimento de Produto
│   ├── Execução rápida
│   ├── Requisitos técnicos
│   ├── Pré-dimensionamento
│   ├── Arquitetura
│   ├── Longarina
│   ├── Chassi
│   ├── Caixa de carga
│   ├── Sistemas e acessórios
│   ├── Rodagem
│   ├── Fornecedores
│   ├── CAE
│   ├── Protótipo técnico
│   ├── Gates técnicos
│   └── Databook técnico
├── 4. Revisão, Aprovação e Liberação
├── 5. Produção e Protótipo
├── 6. Verificação e Validação
├── 7. Homologação e Configurador
└── 8. Pós-lançamento e Alterações
```

## 6. Classificação dos destinos

A matriz utiliza cinco classificações:

| Classificação | Definição |
|---|---|
| **MIGRAR** | A atividade passa a ser executada no módulo Desenvolvimento de Produto. |
| **PERMANECER** | A atividade continua no processo macro do FEK Flow. |
| **GATE** | A atividade deixa de ser execução e passa a ser critério de aprovação. |
| **EVIDÊNCIA** | A atividade é absorvida por outra execução e seu resultado passa a ser evidência. |
| **REALOCAR** | A atividade pertence a outra etapa macro do FEK Flow. |

## 7. Matriz de correspondência — Estrutura

| Atividade atual do FEK Flow | Classificação | Destino proposto | Justificativa |
|---|---|---|---|
| Determinar capacidade de carga | MIGRAR | Requisitos / Pré-dimensionamento | É entrada técnica para distribuição de carga e dimensionamento. |
| Definir geometria geral | MIGRAR | Arquitetura do produto | A geometria interliga requisitos, acoplamento, suspensão e caixa de carga. |
| Calcular distribuição de carga | MIGRAR | Pré-dimensionamento estrutural | É cálculo técnico especializado e deve produzir memória de cálculo. |
| Determinar reações no pino-rei e suspensão | MIGRAR | Pré-dimensionamento estrutural | Resultado técnico utilizado na arquitetura e dimensionamento. |
| Verificar PBT e PBTC | MIGRAR + GATE | Pré-dimensionamento / Gate técnico | O cálculo ocorre no módulo; a conformidade compõe o gate. |
| Definir eixos e suspensão | MIGRAR | Requisitos / Arquitetura / Rodagem | Interfere diretamente na configuração e distribuição de carga. |
| Selecionar matéria-prima | MIGRAR | Longarina / Chassi / Caixa de carga | A seleção deve ser vinculada ao componente e às propriedades mecânicas. |
| Verificar limites dimensionais | MIGRAR + GATE | Requisitos / Arquitetura / Validação | A verificação ocorre durante o desenvolvimento e consolida gate de conformidade. |
| Analisar interferências | MIGRAR | Arquitetura / Chassi / Acessórios | Deve ocorrer continuamente no modelo completo. |
| Gerar modelo 3D e desenhos | MIGRAR + EVIDÊNCIA | Longarina / Chassi / Caixa / PDM | A execução pertence ao módulo; arquivos oficiais permanecem no PDM. |
| Executar FEA quando aplicável | MIGRAR | Estratégia CAE / FEK Kernel | A preparação e rastreabilidade ficam no módulo; o processamento pode usar solver externo. |

## 8. Matriz de correspondência — Caixa e acabamento

| Atividade atual do FEK Flow | Classificação | Destino proposto | Justificativa |
|---|---|---|---|
| Dimensionar caixa de carga | MIGRAR | Caixa de carga | É parte funcional central do produto. |
| Definir capacidade volumétrica | MIGRAR | Requisitos / Caixa de carga | Deve ser ligada ao envelope da carga e configuração operacional. |
| Selecionar matéria-prima | MIGRAR | Caixa de carga / Material | Deve ser vinculada aos componentes e critérios estruturais/produtivos. |
| Definir sinalização e faixas refletivas | MIGRAR | Sistemas e acessórios | É requisito de conformidade e integração física do produto. |
| Gerar modelos e desenhos | MIGRAR + EVIDÊNCIA | Caixa de carga / PDM | O desenvolvimento ocorre no módulo e a liberação oficial permanece no PDM. |

## 9. Matriz de correspondência — Montagem

| Atividade atual do FEK Flow | Classificação | Destino proposto | Justificativa |
|---|---|---|---|
| Realizar montagem geral 3D | MIGRAR | Chassi / Sistemas / Rodagem | Representa a integração física completa do produto. |
| Simular movimentos | MIGRAR | Integração e validação final | Pode envolver varredura, interferências ou mecanismos. |
| Analisar montabilidade | MIGRAR + GATE | Chassi / Validação / Gate multidisciplinar | A análise técnica ocorre no módulo; o parecer produtivo compõe o gate corporativo. |
| Verificar acesso de ferramentas | MIGRAR + GATE | Chassi / Acessórios / Validação | É critério de fabricabilidade e manutenção. |
| Gerar instrução de montagem | EVIDÊNCIA + REALOCAR | Revisão e Liberação / Produção | O módulo fornece dados técnicos; a instrução liberada pertence ao processo produtivo. |
| Gerar prospecto e desenho para AET | REALOCAR | Homologação e Configurador | É documentação regulatória/comercial posterior ao desenvolvimento técnico. |

## 10. Matriz de correspondência — Sistemas

| Atividade atual do FEK Flow | Classificação | Destino proposto | Justificativa |
|---|---|---|---|
| Definir suspensão | MIGRAR | Requisitos / Arquitetura / Rodagem | A suspensão é configuração técnica do produto. |
| Dimensionar suportes e vigas de eixo | MIGRAR | Chassi / Cálculo estrutural | É componente estrutural da interface eixo–chassi. |
| Definir sistema hidráulico | MIGRAR condicional | Sistemas e acessórios | Deve ser criado somente quando aplicável à configuração. |
| Definir sistema pneumático | MIGRAR | Sistemas e acessórios | O sistema pneumático geral independe do tipo de suspensão. |
| Definir sistema elétrico | MIGRAR | Sistemas e acessórios | Integração técnica necessária à configuração. |
| Gerar diagramas e listas técnicas | MIGRAR + EVIDÊNCIA | Sistemas e acessórios / PDM/ERP | O módulo gera e rastreia; os documentos oficiais permanecem nos sistemas corporativos. |

## 11. Nova função da etapa 3 no FEK Flow

A etapa **3. Detalhamento Multidisciplinar** será renomeada para:

> **3. Desenvolvimento de Produto**

Ela não deve repetir todas as atividades técnicas. Sua função macro será:

1. criar ou associar o workspace técnico do produto;
2. confirmar a baseline de requisitos técnicos;
3. acompanhar progresso operacional;
4. acompanhar maturidade técnica;
5. consolidar participação multidisciplinar;
6. registrar decisões e desvios críticos;
7. receber evidências principais;
8. aprovar o gate de conclusão do desenvolvimento técnico;
9. liberar o projeto para revisão documental e produtiva.

## 12. Atividades macro propostas para o FEK Flow

| Código proposto | Atividade macro | Tipo |
|---|---|---|
| DEV-001 | Criar ou associar o Desenvolvimento de Produto | Governança |
| DEV-002 | Confirmar escopo e baseline técnica | Gate de entrada |
| DEV-003 | Designar disciplinas e responsáveis participantes | Governança |
| DEV-004 | Acompanhar progresso operacional e maturidade técnica | Monitoramento |
| DEV-005 | Consolidar decisões, desvios e riscos críticos | Governança |
| DEV-006 | Validar integração entre estrutura, caixa, sistemas e componentes | Gate multidisciplinar |
| DEV-007 | Conferir evidências técnicas obrigatórias | Gate de evidências |
| DEV-008 | Aprovar conclusão do desenvolvimento técnico | Gate de saída |
| DEV-009 | Liberar para revisão, aprovação e documentação oficial | Transição |

## 13. Dados que o módulo deve retornar ao FEK Flow

O FEK Flow não precisa receber toda a estrutura interna do módulo. Deve receber um resumo versionado:

```json
{
  "productDevelopmentId": "PD-2026-001",
  "projectId": "PRJ-2026-001",
  "operationalProgress": 68,
  "technicalMaturity": 40,
  "currentTechnicalGate": "G04",
  "health": "attention",
  "criticalBlockers": 2,
  "pendingValidations": 3,
  "mainEvidence": [],
  "updatedAt": "2026-07-31T00:00:00-03:00"
}
```

## 14. Regras de integração

1. Um projeto do FEK Flow pode possuir no máximo um Desenvolvimento de Produto ativo por configuração.
2. Derivações podem referenciar um projeto técnico anterior, mas devem possuir histórico próprio.
3. O FEK Flow não deve duplicar atividades internas do módulo.
4. Gates técnicos pertencem ao módulo; gates corporativos pertencem ao FEK Flow.
5. O avanço técnico pode ocorrer de maneira concorrente.
6. Bloqueios reais devem ser explícitos; dependências orientativas devem gerar alerta, não impedimento.
7. Evidências devem possuir origem, revisão, responsável e data.
8. A aprovação da etapa 3 depende da maturidade mínima e das evidências definidas, não de um percentual isolado.
9. O FEK Kernel deve ser acionado por interfaces do Engineering Model, sem leitura direta de arquivos pelo FEK Flow.
10. Modelos CAD, desenhos e BOM oficiais não devem ser duplicados no banco do FEK Flow.

## 15. Migração dos projetos existentes

A migração deve preservar os dados existentes.

### 15.1 Atividades concluídas

- converter em evidências ou marcos concluídos no novo módulo;
- preservar responsável, resultado, data e anexos;
- não exigir nova execução sem justificativa técnica.

### 15.2 Atividades em andamento

- mapear para a atividade equivalente do módulo;
- manter responsável, prioridade e observações;
- registrar a origem como `legacy-fek-flow`.

### 15.3 Atividades pendentes

- não copiar automaticamente quando a nova regra já gerar uma atividade equivalente;
- evitar duplicidade por título, disciplina e finalidade.

### 15.4 Atividades sem correspondência

- classificar como atividade avulsa de governança;
- submeter à revisão manual antes da migração.

## 16. Alterações proibidas nesta etapa

Esta especificação não autoriza ainda:

- apagar a etapa atual do `collab.html`;
- alterar projetos já existentes;
- copiar o HTML standalone para dentro do FEK Flow;
- modificar a API central;
- alterar o banco de dados;
- remover registros históricos;
- unificar gates técnicos e corporativos;
- iniciar migração automática sem teste controlado.

## 17. Critérios de aceitação da arquitetura

A arquitetura será considerada aprovada quando:

- cada atividade atual possuir destino definido;
- não houver atividade técnica sem sistema proprietário;
- a etapa 3 possuir função macro clara;
- gates técnicos e corporativos estiverem separados;
- dados de retorno do módulo estiverem definidos;
- regras de migração preservarem histórico;
- a implementação puder ocorrer sem duplicar tarefas;
- a integração permanecer compatível com o modelo multiusuário do FEK Flow.

## 18. Próxima implementação autorizada após validação

Após aprovação desta FES, o próximo passo será exclusivamente:

> **Extrair a definição do workflow técnico da constante monolítica `template` e criar um módulo de dados separado, sem alterar ainda a interface nem os projetos existentes.**

A implementação deverá ser validada por comparação entre:

- quantidade de etapas antes e depois;
- atividades macro preservadas;
- atividades técnicas removidas do template corporativo;
- geração correta de novos projetos;
- preservação de projetos antigos;
- integridade do Workspace, Kanban, Dashboard e Registros.

---

## 19. Status da FES

**Arquitetura:** definida  
**Implementação:** não iniciada  
**Validação do usuário:** pendente  
**Alteração de código:** não realizada nesta revisão  
