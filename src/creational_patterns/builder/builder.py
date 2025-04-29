from typing import Optional

from src.creational_patterns.builder.model import Computer
from src.logger import Logger


class ComputerBuilder:
    def __init__(self) -> None:
        self._computer = Computer()

    def build(self) -> Computer:
        return self._computer

    # ========== Getter methods ==========
    @property
    def cpu(self) -> Optional[str]:
        return self._computer.cpu

    @property
    def ram(self) -> Optional[int]:
        return self._computer.ram

    @property
    def storage(self) -> Optional[int]:
        return self._computer.storage

    @property
    def gpu(self) -> Optional[str]:
        return self._computer.gpu

    @property
    def power_supply(self) -> Optional[int]:
        return self._computer.power_supply

    # ========== Setter methods ==========
    def set_cpu(self, cpu: str) -> "ComputerBuilder":
        self._computer.cpu = cpu
        return self

    def set_ram(self, ram: int) -> "ComputerBuilder":
        self._computer.ram = ram
        return self

    def set_storage(self, storage: int) -> "ComputerBuilder":
        self._computer.storage = storage
        return self

    def set_gpu(self, gpu: str) -> "ComputerBuilder":
        self._computer.gpu = gpu
        return self

    def set_power_supply(self, power_supply: int) -> "ComputerBuilder":
        self._computer.power_supply = power_supply
        return self


# --- Example Usage ---
if __name__ == "__main__":
    logger = Logger("BuilderLogger").get_logger()

    computer = (
        ComputerBuilder()
        .set_cpu("AMD Ryzen 9")
        .set_ram(32)
        .set_storage(1000)
        .set_gpu("NVIDIA RTX 3090")
        .set_power_supply(500)
        .build()
    )

    logger.info(computer)
