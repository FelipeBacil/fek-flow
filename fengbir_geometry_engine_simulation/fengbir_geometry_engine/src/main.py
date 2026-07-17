"""Motor Geométrico 2D Fengbir - MVP 01.1.

Modos:
- section: seção transversal. Calcula área, Ix, Iy, Wx, Wy e massa por metro.
- plate: vista lateral/chapa plana. Calcula área plana, envelope, volume e massa total.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from shapely.geometry import Polygon

from dxf_reader import read_closed_lwpolyline
from geometry_validator import validate_polygon
from material_database import get_material
from plate_properties import plate_properties
from plotter import save_section_plot
from report_generator import save_markdown_report
from section_properties import polygon_section_properties


def run(
    filepath: str,
    component: str,
    material_key: str,
    output_dir: str = "output",
    mode: str = "section",
    thickness_mm: float | None = None,
) -> dict:
    source = Path(filepath)
    out = Path(output_dir)
    json_dir = out / "json"
    img_dir = out / "imagens"
    report_dir = out / "relatorios"
    json_dir.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    points = read_closed_lwpolyline(source)
    validation = validate_polygon(points)
    if validation["status"] != "ok":
        raise ValueError(validation["message"])

    material = get_material(material_key)
    polygon = Polygon(points)

    if mode == "section":
        props = polygon_section_properties(points)
        props["perimeter_mm"] = float(polygon.length)
        area_m2 = props["area_mm2"] / 1_000_000
        props["volume_m3_per_m"] = area_m2
        props["mass_kg_per_m"] = area_m2 * material["density_kg_m3"]
        geometry_type = "2D_section"
    elif mode == "plate":
        if thickness_mm is None:
            raise ValueError("No modo plate, informe --thickness, por exemplo: --thickness 6.35")
        props = plate_properties(points, thickness_mm, material["density_kg_m3"])
        geometry_type = "2D_plate"
    else:
        raise ValueError("Modo inválido. Use --mode section ou --mode plate")

    result = {
        "component": component,
        "geometry_type": geometry_type,
        "source_file": source.name,
        "unit": "mm",
        "material": material,
        "properties": props,
        "validation": validation,
    }

    stem = source.stem
    suffix = mode
    json_path = json_dir / f"{stem}_{suffix}_properties.json"
    img_path = img_dir / f"{stem}_{suffix}.png"
    report_path = report_dir / f"{stem}_{suffix}_report.md"

    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    save_section_plot(points, (props["centroid_x_mm"], props["centroid_y_mm"]), img_path)
    save_markdown_report(result, report_path)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Motor Geométrico 2D Fengbir - MVP 01.1")
    parser.add_argument("filepath", help="Caminho do DXF com contorno 2D fechado")
    parser.add_argument("--component", default="longarina", help="Nome do componente")
    parser.add_argument("--material", default="ACO_CARBONO", help="Código do material")
    parser.add_argument("--output", default="output", help="Pasta de saída")
    parser.add_argument("--mode", choices=["section", "plate"], default="section", help="Tipo de leitura geométrica")
    parser.add_argument("--thickness", type=float, default=None, help="Espessura em mm para modo plate")
    args = parser.parse_args()

    result = run(args.filepath, args.component, args.material, args.output, args.mode, args.thickness)
    print(json.dumps(result, indent=2, ensure_ascii=False))
