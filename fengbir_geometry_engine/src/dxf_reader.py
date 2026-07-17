"""Leitor DXF simplificado para contornos 2D fechados."""
from __future__ import annotations

import math
from pathlib import Path
from typing import List, Tuple

import ezdxf

Point = Tuple[float, float]


def _arc_points(center, radius, start_angle, end_angle, segments=24) -> List[Point]:
    """Discretiza arco em pontos."""
    if end_angle < start_angle:
        end_angle += 360
    angles = [math.radians(start_angle + (end_angle - start_angle) * i / segments) for i in range(segments + 1)]
    return [(center[0] + radius * math.cos(a), center[1] + radius * math.sin(a)) for a in angles]


def read_closed_lwpolyline(filepath: str | Path) -> List[Point]:
    """
    Lê a primeira LWPOLYLINE fechada do DXF.

    MVP: prioriza LWPOLYLINE. Arcos com bulge ainda são tratados como segmentos retos
    entre vértices; em versão futura, o bulge será discretizado corretamente.
    """
    doc = ezdxf.readfile(filepath)
    msp = doc.modelspace()

    for entity in msp.query("LWPOLYLINE"):
        points = [(float(p[0]), float(p[1])) for p in entity.get_points()]
        if entity.closed or (points and points[0] == points[-1]):
            return points

    # Fallback simples: tenta POLYLINE fechada
    for entity in msp.query("POLYLINE"):
        if entity.is_closed:
            return [(float(v.dxf.location.x), float(v.dxf.location.y)) for v in entity.vertices]

    raise ValueError("Nenhuma LWPOLYLINE/POLYLINE fechada encontrada no DXF.")
