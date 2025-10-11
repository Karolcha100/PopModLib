from typing import TypeVar, Generic, Type

T = TypeVar("T", bound="StrategyFactory")

class StrategyFactory:
    def __init__(self, strategy_id: str, modules: dict[str, object]) -> None:
        self.strategy_id = strategy_id
        self.modules = modules
        for name, module in modules.items():
            setattr(self, name, module)

    @classmethod
    def create(cls: Type[T], strategy_id: str, **modules: object) -> T:
        """Tworzy instancję i przypisuje moduły jako atrybuty"""
        instance = cls(strategy_id, modules)
        return instance
