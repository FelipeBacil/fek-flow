# FES-002
# Geometry Model
## Modelo Geométrico do FEK

**Versão:** 0.1

---

# Objetivo

Definir como o FEK representa geometricamente um arquivo CAD após sua leitura.

O Geometry Model é a primeira camada estruturada após a importação de arquivos STEP, DXF ou outros formatos CAD.

---

# Entidades Principais

O modelo geométrico será composto por:

- Assembly
- Body
- Face
- Edge
- Vertex

---

# Assembly

Representa o conjunto importado.

Deve conter:

- ID da montagem
- nome do arquivo de origem
- quantidade de corpos
- massa total
- volume total
- bounding box global
- lista de corpos

---

# Body

Representa cada sólido encontrado no arquivo CAD.

Deve conter:

- ID do corpo
- índice do corpo
- volume
- massa
- área superficial
- centro de massa
- bounding box
- lista de faces
- lista de arestas
- lista de vértices

---

# Face

Representa cada superfície do corpo.

Deve conter:

- ID da face
- índice da face
- tipo geométrico
- área
- centro
- bounding box
- normal futura
- loops futuros
- arestas associadas

Tipos esperados:

- PLANE
- CYLINDER
- CONE
- SPHERE
- TORUS
- UNKNOWN

---

# Edge

Representa cada aresta.

Deve conter:

- ID da aresta
- índice da aresta
- tipo de curva
- comprimento
- vértices inicial e final
- faces adjacentes futuras

---

# Vertex

Representa cada ponto topológico.

Deve conter:

- ID do vértice
- índice do vértice
- coordenadas X, Y, Z

---

# Princípio Fundamental

Nenhuma informação geométrica deve ser descartada.

Toda entidade lida do CAD deverá ser preservada no modelo interno para uso futuro pelos módulos estruturais, dinâmicos, de malha e de simulação.

---

# Estado Atual Implementado

O FEK já executa:

- leitura de STEP
- leitura de múltiplos sólidos
- cálculo de volume por sólido
- cálculo de massa por sólido
- cálculo de massa total
- mapeamento de faces
- classificação básica de tipo de face
- contagem de arestas
- contagem de vértices

---

# Próximas Implementações

- criar IDs persistentes para Assembly, Body, Face, Edge e Vertex
- mapear arestas individualmente
- mapear vértices individualmente
- criar adjacência entre faces
- identificar loops externos e internos
- preparar dados para geração de malha