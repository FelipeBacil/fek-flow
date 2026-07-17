from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.export_dashboard import (
    build_dashboard_payload,
    calculate_summary,
    export_dashboard,
)


class TestDashboardExporter(unittest.TestCase):
    def test_calculate_summary(self) -> None:
        modules = [
            {"status": "completed", "progress": 100},
            {"status": "in_progress", "progress": 50},
            {"status": "planned", "progress": 0},
        ]

        summary = calculate_summary(modules)

        self.assertEqual(summary["modules_total"], 3)
        self.assertEqual(summary["modules_completed"], 1)
        self.assertEqual(summary["modules_in_progress"], 1)
        self.assertEqual(summary["modules_planned"], 1)
        self.assertEqual(summary["overall_progress"], 50.0)

    def test_build_dashboard_payload(self) -> None:
        activity_index = {
            "schema_version": "1.0.0",
            "project": {
                "id": "FEK",
                "name": "Fengbir Engineering Kernel",
                "status": "active",
            },
            "modules": [],
        }

        payload = build_dashboard_payload(activity_index)

        self.assertEqual(payload["project"]["id"], "FEK")
        self.assertEqual(payload["summary"]["modules_total"], 0)
        self.assertIn("generated_at", payload)

    def test_export_dashboard_file(self) -> None:
        source_payload = {
            "schema_version": "1.0.0",
            "project": {
                "id": "FEK",
                "name": "Fengbir Engineering Kernel",
                "status": "active",
            },
            "modules": [
                {
                    "id": "core",
                    "name": "Core",
                    "status": "active",
                    "progress": 25,
                    "activities": [],
                }
            ],
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            source_file = temp_path / "activity-index.json"
            export_file = temp_path / "fek-dashboard.json"

            source_file.write_text(
                json.dumps(source_payload),
                encoding="utf-8",
            )

            result = export_dashboard(source_file, export_file)

            self.assertEqual(result, export_file)
            self.assertTrue(export_file.exists())

            exported_payload = json.loads(
                export_file.read_text(encoding="utf-8")
            )

            self.assertEqual(
                exported_payload["summary"]["modules_active"],
                1,
            )
            self.assertEqual(
                exported_payload["summary"]["overall_progress"],
                25.0,
            )


if __name__ == "__main__":
    unittest.main()
