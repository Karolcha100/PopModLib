from abc import ABC, abstractmethod



class EnergyTemplate(ABC):
    """
    Template for energy-based reproduction strategies.
    """
    @abstractmethod
    def if_reproduce(self, current_value: float) -> bool:
        pass

    @abstractmethod
    def get_energy_for_child(self) -> float:
        pass

    @abstractmethod
    def get_total_parent_energy_loss(self) -> float:
        pass



class FlatConditionEnergy(EnergyTemplate):
    def __init__(
            self, 
            condition_value : float,
            energy_for_child : float,
            energy_additional_loss : float = 0.0,
        ) -> None:

        self.condition_value : float = condition_value
        self.energy_for_child : float = energy_for_child
        self.energy_additional_loss : float = energy_additional_loss

    def if_reproduce(self, current_value : float) -> bool:
        return current_value >= self.condition_value

    def get_energy_for_child(self) -> float:
        return self.energy_for_child
    
    def get_total_parent_energy_loss(self) -> float:
        return self.energy_for_child + self.energy_additional_loss
    
