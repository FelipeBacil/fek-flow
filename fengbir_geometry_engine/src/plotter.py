"""Geração de imagem da seção."""
from __future__ import annotations

from pathlib import Path
from typing import Sequence, Tuple

import matplotlib.pyplot as plt

Point = Tuple[float, float]


def save_section_plot(points: Sequence[Point], centroid: Tuple[float, float], output_path: str | Path) -> None:
    pts = list(points)
    if pts[0] != pts[-1]:
        pts.append(pts[0])

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    plt.figure(figsize=(8, 6))
    plt.plot(xs, ys, marker="o")
    plt.scatter([centroid[0]], [centroid[1]], marker="x", s=80)
    plt.axis("equal")
    plt.grid(True)
    plt.title("Seção 2D - Motor Geométrico Fengbir")
    plt.xlabel("x [mm]")
    plt.ylabel("y [mm]")
    plt.tight_layout()
    plt.savefig(output_path, dpi=160)
    plt.close()
