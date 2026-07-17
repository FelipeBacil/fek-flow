# FES-003
# Topology Model
## Modelo Topológico do FEK

Versão: 0.1

---

# Objetivo

Definir como o FEK representa as relações entre entidades geométricas.

O modelo topológico transforma uma coleção de faces em uma estrutura inteligente capaz de compreender continuidade, espessuras, furos e regiões estruturais.

---

# Hierarquia

Assembly

↓

Bodies

↓

Faces

↓

Loops

↓

Edges

↓

Vertices

---

# Face

Cada face deverá conhecer:

- seu Body
- suas Edges
- seus Loops
- suas Faces vizinhas
- sua normal
- seu tipo geométrico

---

# Loop

Cada Face pode possuir um ou mais Loops.

Loop Externo

Representa o contorno principal.

Loops Internos

Representam:

- furos
- rasgos
- janelas
- vazados

---

# Edge

Cada Edge deverá conhecer:

- vértice inicial
- vértice final
- curva geométrica
- comprimento
- faces adjacentes

---

# Vertex

Cada vértice deverá conhecer:

- coordenadas
- arestas conectadas

---

# Objetivos futuros

Reconhecimento automático de:

- chapas
- espessuras
- furos
- soldas
- reforços
- dobras
- perfis estruturais