from __future__ import annotations

from typing import Self






class ReproductionFactory:
    def __init__(self, modules: dict[str, object]) -> None:
        self._modules = modules
        for name, module in modules.items():
            setattr(self, name, module)

    @classmethod
    def create(cls, **modules: object) -> Self:
        """Tworzy instancję i przypisuje moduły jako atrybuty"""
        instance = cls(modules)
        return instance
