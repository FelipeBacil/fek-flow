"""Geração de relatório simples em Markdown."""
from __future__ import annotations

from pathlib import Path


def save_markdown_report(result: dict, output_path: str | Path) -> None:
    p = result["properties"]
    mat = result["material"]
    text = f"""# Relatório - Motor Geométrico Fengbir

## Componente

- Tipo: {result['component']}
- Arquivo: {result['source_file']}
- Unidade: {result['unit']}

## Material

- Material: {mat['name']}
- Densidade: {mat['density_kg_m3']} kg/m³
- Limite de escoamento: {mat['yield_strength_mpa']} MPa

## Propriedades geométricas

- Área: {p['area_mm2']:.3f} mm²
- Perímetro: {p['perimeter_mm']:.3f} mm
- Centroide X: {p['centroid_x_mm']:.3f} mm
- Centroide Y: {p['centroid_y_mm']:.3f} mm
- Ix: {p['Ix_mm4']:.3f} mm⁴
- Iy: {p['Iy_mm4']:.3f} mm⁴
- Ixy: {p['Ixy_mm4']:.3f} mm⁴
- Wx: {p['Wx_mm3']:.3f} mm³
- Wy: {p['Wy_mm3']:.3f} mm³
- rx: {p['rx_mm']:.3f} mm
- ry: {p['ry_mm']:.3f} mm
- Massa por metro: {p['mass_kg_per_m']:.3f} kg/m

## Validação

- Status: {result['validation']['status']}
- Mensagem: {result['validation']['message']}
"""
    Path(output_path).write_text(text, encoding="utf-8")
