from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "management" / "activity-index.json"
EXPORT_FILE = ROOT / "management" / "exports" / "fek-dashboard.json"


def load_activity_index(path: Path = SOURCE_FILE) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(
            f"Arquivo de origem não encontrado: {path}"
        )

    with path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    if "project" not in payload:
        raise ValueError("activity-index.json não contém o campo 'project'.")

    if "modules" not in payload or not isinstance(payload["modules"], list):
        raise ValueError(
            "activity-index.json não contém uma lista válida em 'modules'."
        )

    return payload


def calculate_summary(modules: list[dict[str, Any]]) -> Dict[str, Any]:
    total = len(modules)
    status_counts = {
        "planned": 0,
        "in_progress": 0,
        "active": 0,
        "blocked": 0,
        "completed": 0,
    }

    progress_values: list[float] = []

    for module in modules:
        status = str(module.get("status", "planned"))
        if status in status_counts:
            status_counts[status] += 1

        progress = module.get("progress", 0)
        if isinstance(progress, (int, float)):
            progress_values.append(max(0.0, min(float(progress), 100.0)))
        else:
            progress_values.append(0.0)

    overall_progress = (
        round(sum(progress_values) / total, 2)
        if total
        else 0.0
    )

    return {
        "modules_total": total,
        "modules_planned": status_counts["planned"],
        "modules_in_progress": status_counts["in_progress"],
        "modules_active": status_counts["active"],
        "modules_blocked": status_counts["blocked"],
        "modules_completed": status_counts["completed"],
        "overall_progress": overall_progress,
    }


def build_dashboard_payload(
    activity_index: Dict[str, Any]
) -> Dict[str, Any]:
    modules = activity_index["modules"]

    return {
        "schema_version": activity_index.get("schema_version", "1.0.0"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": activity_index["project"],
        "summary": calculate_summary(modules),
        "modules": modules,
    }


def export_dashboard(
    source_path: Path = SOURCE_FILE,
    export_path: Path = EXPORT_FILE,
) -> Path:
    activity_index = load_activity_index(source_path)
    dashboard_payload = build_dashboard_payload(activity_index)

    export_path.parent.mkdir(parents=True, exist_ok=True)

    with export_path.open("w", encoding="utf-8") as file:
        json.dump(
            dashboard_payload,
            file,
            ensure_ascii=False,
            indent=2,
        )
        file.write("\n")

    return export_path


def main() -> None:
    exported_file = export_dashboard()
    print("FEK Dashboard Exporter")
    print(f"Source: {SOURCE_FILE}")
    print(f"Export: {exported_file}")
    print("Dashboard export completed successfully.")


if __name__ == "__main__":
    main()
