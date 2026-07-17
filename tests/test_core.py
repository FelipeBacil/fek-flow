from pathlib import Path
import sys
import unittest

SRC_PATH = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_PATH))

from core import KernelInfo, ModuleRecord, ModuleStatus, __version__


class TestKernelInfo(unittest.TestCase):
    def test_kernel_uses_official_version(self) -> None:
        kernel = KernelInfo()
        self.assertEqual(kernel.identifier, "FEK")
        self.assertEqual(kernel.version, __version__)

    def test_register_and_retrieve_module(self) -> None:
        kernel = KernelInfo()
        geometry = ModuleRecord(
            module_id="geometry_engine",
            name="Geometry Engine",
            status=ModuleStatus.IN_PROGRESS,
            version="0.1.0",
            description="Interpretação geométrica de modelos CAD.",
        )
        kernel.register_module(geometry)
        self.assertEqual(kernel.get_module("geometry_engine"), geometry)
        self.assertEqual(len(kernel.list_modules()), 1)

    def test_duplicate_module_is_rejected(self) -> None:
        kernel = KernelInfo()
        module = ModuleRecord(
            module_id="core",
            name="Core",
            status=ModuleStatus.ACTIVE,
            version=__version__,
        )
        kernel.register_module(module)
        with self.assertRaises(ValueError):
            kernel.register_module(module)

    def test_export_to_dict(self) -> None:
        kernel = KernelInfo()
        kernel.register_module(
            ModuleRecord(
                module_id="core",
                name="Core",
                status=ModuleStatus.ACTIVE,
                version=__version__,
            )
        )
        payload = kernel.to_dict()
        self.assertEqual(payload["kernel"]["identifier"], "FEK")
        self.assertEqual(payload["modules"][0]["status"], "active")


if __name__ == "__main__":
    unittest.main()
