"""Cálculo de propriedades para chapas/peças planas 2D fechadas."""
from __future__ import annotations

from typing import Dict, Sequence, Tuple

from shapely.geometry import Polygon

Point = Tuple[float, float]


def plate_properties(points: Sequence[Point], thickness_mm: float, density_kg_m3: float) -> Dict[str, float]:
    """Calcula propriedades de uma peça plana a partir do contorno externo.

    Entrada: coordenadas em mm, espessura em mm, densidade em kg/m³.
    Saída: área plana, perímetro, envelope, volume e massa da peça.
    """
    if thickness_mm <= 0:
        raise ValueError("A espessura deve ser maior que zero.")

    polygon = Polygon(points)
    if not polygon.is_valid or polygon.area <= 0:
        raise ValueError("Geometria inválida para cálculo de chapa.")

    xmin, ymin, xmax, ymax = polygon.bounds
    area_mm2 = float(polygon.area)
    perimeter_mm = float(polygon.length)
    centroid = polygon.centroid

    volume_mm3 = area_mm2 * thickness_mm
    volume_m3 = volume_mm3 / 1_000_000_000
    mass_kg = volume_m3 * density_kg_m3

    return {
        "area_planar_mm2": area_mm2,
        "area_planar_m2": area_mm2 / 1_000_000,
        "perimeter_mm": perimeter_mm,
        "centroid_x_mm": float(centroid.x),
        "centroid_y_mm": float(centroid.y),
        "xmin_mm": float(xmin),
        "xmax_mm": float(xmax),
        "ymin_mm": float(ymin),
        "ymax_mm": float(ymax),
        "length_mm": float(xmax - xmin),
        "height_mm": float(ymax - ymin),
        "thickness_mm": float(thickness_mm),
        "volume_mm3": volume_mm3,
        "volume_m3": volume_m3,
        "mass_kg": mass_kg,
        "mass_kg_per_m_length": mass_kg / ((xmax - xmin) / 1000) if xmax > xmin else 0.0,
    }
