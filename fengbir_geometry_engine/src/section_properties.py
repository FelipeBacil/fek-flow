"""Cálculo de propriedades geométricas de uma seção 2D fechada."""
from __future__ import annotations

import math
from typing import Sequence, Tuple, Dict

Point = Tuple[float, float]


def polygon_section_properties(points: Sequence[Point]) -> Dict[str, float]:
    """
    Calcula área, centroide, Ix, Iy e Ixy para polígono fechado.

    Entrada em mm. Saída em mm², mm³ e mm⁴.
    Fórmulas poligonais via Teorema de Green.
    """
    if len(points) < 3:
        raise ValueError("A seção precisa ter pelo menos 3 pontos.")

    pts = list(points)
    if pts[0] != pts[-1]:
        pts.append(pts[0])

    a2 = 0.0
    cx_num = 0.0
    cy_num = 0.0
    ix0 = 0.0
    iy0 = 0.0
    ixy0 = 0.0

    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        cross = x0 * y1 - x1 * y0
        a2 += cross
        cx_num += (x0 + x1) * cross
        cy_num += (y0 + y1) * cross
        ix0 += (y0**2 + y0 * y1 + y1**2) * cross
        iy0 += (x0**2 + x0 * x1 + x1**2) * cross
        ixy0 += (x0 * y1 + 2 * x0 * y0 + 2 * x1 * y1 + x1 * y0) * cross

    area_signed = a2 / 2.0
    if abs(area_signed) < 1e-9:
        raise ValueError("Área nula ou geometria inválida.")

    cx = cx_num / (6.0 * area_signed)
    cy = cy_num / (6.0 * area_signed)

    ix_origin = ix0 / 12.0
    iy_origin = iy0 / 12.0
    ixy_origin = ixy0 / 24.0

    # Translação para eixos centroidais
    ix_c = ix_origin - area_signed * cy**2
    iy_c = iy_origin - area_signed * cx**2
    ixy_c = ixy_origin - area_signed * cx * cy

    # Normaliza orientação horária/anti-horária
    area = abs(area_signed)
    ix_c = abs(ix_c)
    iy_c = abs(iy_c)
    ixy_c = abs(ixy_c)

    xs = [p[0] for p in pts[:-1]]
    ys = [p[1] for p in pts[:-1]]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    y_top = abs(ymax - cy)
    y_bottom = abs(cy - ymin)
    x_right = abs(xmax - cx)
    x_left = abs(cx - xmin)

    wx = ix_c / max(y_top, y_bottom) if max(y_top, y_bottom) > 0 else 0.0
    wy = iy_c / max(x_right, x_left) if max(x_right, x_left) > 0 else 0.0

    rx = math.sqrt(ix_c / area) if area > 0 else 0.0
    ry = math.sqrt(iy_c / area) if area > 0 else 0.0

    return {
        "area_mm2": area,
        "centroid_x_mm": cx,
        "centroid_y_mm": cy,
        "Ix_mm4": ix_c,
        "Iy_mm4": iy_c,
        "Ixy_mm4": ixy_c,
        "Wx_mm3": wx,
        "Wy_mm3": wy,
        "rx_mm": rx,
        "ry_mm": ry,
        "xmin_mm": xmin,
        "xmax_mm": xmax,
        "ymin_mm": ymin,
        "ymax_mm": ymax,
        "width_mm": xmax - xmin,
        "height_mm": ymax - ymin,
    }
