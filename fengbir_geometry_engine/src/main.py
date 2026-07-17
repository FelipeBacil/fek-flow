"""MVP 01 - Motor Geométrico 2D Fengbir."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from shapely.geometry import Polygon

from dxf_reader import read_closed_lwpolyline
from geometry_validator import validate_polygon
from material_database import get_material
from plotter import save_section_plot
from report_generator import save_markdown_report
from section_properties import polygon_section_properties


def run(filepath: str, component: str, material_key: str, output_dir: str = "output") -> dict:
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

    props = polygon_section_properties(points)
    polygon = Polygon(points)
    props["perimeter_mm"] = float(polygon.length)

    material = get_material(material_key)
    area_m2 = props["area_mm2"] / 1_000_000
    props["volume_m3_per_m"] = area_m2
    props["mass_kg_per_m"] = area_m2 * material["density_kg_m3"]

    result = {
        "component": component,
        "geometry_type": "2D_section",
        "source_file": source.name,
        "unit": "mm",
        "material": material,
        "properties": props,
        "validation": validation,
    }

    stem = source.stem
    json_path = json_dir / f"{stem}_properties.json"
    img_path = img_dir / f"{stem}_section.png"
    report_path = report_dir / f"{stem}_report.md"

    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    save_section_plot(points, (props["centroid_x_mm"], props["centroid_y_mm"]), img_path)
    save_markdown_report(result, report_path)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Motor Geométrico 2D Fengbir - MVP 01")
    parser.add_argument("filepath", help="Caminho do DXF com contorno 2D fechado")
    parser.add_argument("--component", default="longarina", help="Nome do componente")
    parser.add_argument("--material", default="ACO_CARBONO", help="Código do material")
    parser.add_argument("--output", default="output", help="Pasta de saída")
    args = parser.parse_args()

    result = run(args.filepath, args.component, args.material, args.output)
    print(json.dumps(result, indent=2, ensure_ascii=False))
