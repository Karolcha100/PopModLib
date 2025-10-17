from abc import ABC, abstractmethod



class EnergyTemplate(ABC):
    """
    Template for energy management module for reproduction.
    """
    @abstractmethod
    def if_reproduce(self, current_value: float) -> bool:
        pass

    @abstractmethod
    def get_energy_for_child(self, parent_energy : float) -> float:
        pass

    @abstractmethod
    def get_energy_for_parent(self, parent_energy : float) -> float:
        pass



class FlatConditionEnergy(EnergyTemplate):
    """
    Energy management module for reproduction with flat value as condition for reproduction.

    Args:
        condition_value (float): Value of energy required to reproduce.
        energy_for_child (float): Energy given to child during reproduction.
        energy_additional_loss (float, optional): Additional energy loss for parent during reproduction. Defaults to 0.0.
    """
    def __init__(
            self, 
            condition_value : float,
            energy_for_child : float,
            energy_for_parent : float = 0.0,
        ) -> None:

        self._condition_value : float = condition_value
        self._energy_for_child : float = energy_for_child
        self._energy_for_parent : float = energy_for_parent

    def if_reproduce(self, current_value : float) -> bool:
        return current_value >= self._condition_value

    def get_energy_for_child(self, parent_energy : float) -> float:
        return self._energy_for_child
    
    def get_energy_for_parent(self, parent_energy : float) -> float:
        return self._energy_for_parent
    

class ProportionalEnergyCondition(EnergyTemplate):
    """
    TODO
    """ 
    def __init__(
            self,
            condition_value : float,
            parent_quaranteed_energy: float,
            percentage_energy_for_child : float,
        ) -> None:

        self._condition_value : float = condition_value
        self._parent_quaranteed_energy : float = parent_quaranteed_energy
        self._percentage_energy_for_child : float = percentage_energy_for_child

    def if_reproduce(self, current_value : float) -> bool:
        return current_value >= self._condition_value
    
    def get_energy_for_child(self, parent_energy : float) -> float:
        return (parent_energy - self._parent_quaranteed_energy) * self._percentage_energy_for_child
    
    def get_energy_for_parent(self, parent_energy: float) -> float:
        return (parent_energy - self._parent_quaranteed_energy) * (100 - self._percentage_energy_for_child)



        
    
