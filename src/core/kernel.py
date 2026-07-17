from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Dict, List

from .version import __version__


class ModuleStatus(str, Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    ACTIVE = "active"
    BLOCKED = "blocked"
    COMPLETED = "completed"


@dataclass(frozen=True)
class ModuleRecord:
    module_id: str
    name: str
    status: ModuleStatus = ModuleStatus.PLANNED
    version: str = "0.0.0"
    description: str = ""


@dataclass
class KernelInfo:
    name: str = "Fengbir Engineering Kernel"
    identifier: str = "FEK"
    version: str = __version__
    modules: Dict[str, ModuleRecord] = field(default_factory=dict)

    def register_module(self, module: ModuleRecord) -> None:
        if not module.module_id.strip():
            raise ValueError("module_id não pode ser vazio.")
        if module.module_id in self.modules:
            raise ValueError(
                f"O módulo '{module.module_id}' já está registrado no Kernel."
            )
        self.modules[module.module_id] = module

    def get_module(self, module_id: str) -> ModuleRecord:
        try:
            return self.modules[module_id]
        except KeyError as exc:
            raise KeyError(
                f"O módulo '{module_id}' não está registrado no Kernel."
            ) from exc

    def list_modules(self) -> List[ModuleRecord]:
        return list(self.modules.values())

    def to_dict(self) -> dict:
        return {
            "kernel": {
                "name": self.name,
                "identifier": self.identifier,
                "version": self.version,
            },
            "modules": [
                {**asdict(module), "status": module.status.value}
                for module in self.list_modules()
            ],
        }
