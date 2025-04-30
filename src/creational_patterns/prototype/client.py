from typing import Optional

from src.creational_patterns.prototype.prototype import Car
from src.creational_patterns.prototype.prototype import Vehicle
from src.logger import Logger


# ---------- Registry ----------
class VehicleShowroom:
    """
    A registry that stores and manages vehicle prototypes.
    """

    def __init__(self) -> None:
        self._vehicle_prototypes = {}

    def add_vehicle_prototype(self, name: str, vehicle: Vehicle) -> None:
        """
        Register a vehicle prototype with a given name.
        """
        self._vehicle_prototypes[name] = vehicle

    def remove_vehicle_prototype(self, name: str) -> None:
        """
        Remove a vehicle prototype from the showroom.
        """
        if name in self._vehicle_prototypes:
            del self._vehicle_prototypes[name]

    def get_vehicle_clone(self, name: str) -> Optional[Vehicle]:
        """
        Create and return a clone of the vehicle prototype with the given name.
        """
        prototype = self._vehicle_prototypes.get(name)
        if prototype:
            return prototype.clone()
        return None


# ---------- Client ----------
if __name__ == "__main__":
    logger = Logger("PrototypeLogger").get_logger()

    # Create base vehicle (Car) prototypes
    polestar_prototype = Car(
        brand="Polestar", model="2", color="White", engine_type="Electric"
    )
    logger.info(f"[Polestar prototype] {polestar_prototype.display_info()}")

    # Set up the showroom with prototypes
    showroom = VehicleShowroom()
    showroom.add_vehicle_prototype("Polestar", polestar_prototype)

    # Jacopo's car
    jacopo_car = showroom.get_vehicle_clone("Polestar")
    jacopo_car.add_feature("Turbo")
    jacopo_car.add_feature("Pilot")
    logger.info(f"[Jacopo's car] {jacopo_car.display_info()}")

    # Andrea's car
    andrea_car = showroom.get_vehicle_clone("Polestar")
    andrea_car.color = "Black"
    andrea_car.add_feature("Climate")
    logger.info(f"[Andrea's car] {andrea_car.display_info()}")
