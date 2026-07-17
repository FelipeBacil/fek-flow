# Fengbir Geometry Engine — MVP 01

Motor geométrico 2D para transformar um DXF fechado em propriedades de engenharia.

## Objetivo

Entrada: contorno 2D fechado em DXF.

Saída:

- área;
- perímetro;
- centroide;
- Ix / Iy / Ixy;
- módulo resistente Wx / Wy;
- raio de giração rx / ry;
- massa por metro;
- JSON técnico;
- relatório Markdown;
- imagem da seção.

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

```bash
python src/main.py input/arquivos_dxf/longarina.dxf --component longarina --material S700MC --output output
```

## Observação importante

O MVP 01 prioriza LWPOLYLINE ou POLYLINE fechada. Arcos, splines e geometrias 3D entram nas próximas fases.

## Arquitetura

```text
src/
├── main.py
├── dxf_reader.py
├── geometry_validator.py
├── section_properties.py
├── material_database.py
├── plotter.py
└── report_generator.py
```

## Próximas evoluções

1. Corrigir leitura de bulge em LWPOLYLINE.
2. Suportar furos internos.
3. Suportar múltiplos contornos.
4. Calcular propriedades de chapa dobrada.
5. Integrar com DCL e tensão de flexão.
