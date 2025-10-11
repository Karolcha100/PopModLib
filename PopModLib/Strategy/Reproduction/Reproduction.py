from typing import TypeVar, Generic, Type

T = TypeVar("T", bound="Reproduction")

class Reproduction:
    def __init__(self, modules: dict[str, object]) -> None:
        self.modules = modules
        for name, module in modules.items():
            setattr(self, name, module)

    @classmethod
    def create(cls: Type[T], **modules: object) -> T:
        """Tworzy instancję i przypisuje moduły jako atrybuty"""
        instance = cls(modules)
        return instance
