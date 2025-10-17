from __future__ import annotations

from typing import Self, TYPE_CHECKING








class StrategyFactory:
    def __init__(self, strategy_id: str, modules: dict[str, object]) -> None:
        self._strategy_id = strategy_id
        self._modules = modules
        for name, module in modules.items():
            setattr(self, name, module)

    @classmethod
    def create(cls, strategy_id: str, **modules: object) -> Self:
        """Tworzy instancję i przypisuje moduły jako atrybuty"""
        instance = cls(strategy_id, modules)
        return instance
