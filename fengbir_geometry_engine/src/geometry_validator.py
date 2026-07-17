"""Validação geométrica do contorno."""
from __future__ import annotations

from typing import Sequence, Tuple, Dict
from shapely.geometry import Polygon

Point = Tuple[float, float]


def validate_polygon(points: Sequence[Point]) -> Dict[str, object]:
    """Valida fechamento, área e auto-interseção."""
    if len(points) < 3:
        return {"status": "erro", "message": "Menos de 3 pontos.", "closed_contour": False}

    pts = list(points)
    closed = pts[0] == pts[-1]
    if not closed:
        pts.append(pts[0])

    polygon = Polygon(pts)
    return {
        "status": "ok" if polygon.is_valid and polygon.area > 0 else "erro",
        "closed_contour": True,
        "self_intersection": not polygon.is_valid,
        "area_positive": polygon.area > 0,
        "message": "Geometria válida." if polygon.is_valid and polygon.area > 0 else "Geometria inválida.",
    }
