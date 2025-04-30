from abc import ABC
from abc import abstractmethod
from copy import deepcopy


# ----- Prototype Interface -----
class Vehicle(ABC):
    """
    The Vehicle prototype interface declares the clone method.
    """

    @abstractmethod
    def clone(self):
        """
        Return a new Vehicle instance that is a copy of this vehicle.
        """
        pass

    @abstractmethod
    def display_info(self):
        """
        Display information about the vehicle.
        """
        pass


# ----- Concrete prototypes -----
class Car(Vehicle):
    """
    Concrete Car prototype that implements the clone method.
    """

    def __init__(self, brand: str, model: str, color: str, engine_type: str) -> None:
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.features = []

    def add_feature(self, feature: str) -> None:
        self.features.append(feature)

    def clone(self) -> "Car":
        return deepcopy(self)

    def display_info(self) -> str:
        features_str = ", ".join(self.features) if self.features else "Not specified"

        return (
            f"{self.brand} {self.model} configuration:\n"
            f"  - Color:        {self.color}\n"
            f"  - Engine:       {self.engine_type}\n"
            f"  - Features:     {features_str}"
        )


class Motorcycle(Vehicle):
    """
    Concrete Motorcycle prototype that implements the clone method.
    """

    def __init__(self, brand: str, model: str, color: str, engine_size: int) -> None:
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_size = engine_size
        self.accessories = []

    def add_accessory(self, accessory: str) -> None:
        self.accessories.append(accessory)

    def clone(self) -> "Motorcycle":
        return deepcopy(self)

    def display_info(self) -> str:
        accessories_str = (
            ", ".join(self.accessories) if self.accessories else "Not specified"
        )

        return (
            f"{self.brand} {self.model} configuration:\n"
            f"  - Color:        {self.color}\n"
            f"  - Engine:       {self.engine_size}\n"
            f"  - Features:     {accessories_str}"
        )
