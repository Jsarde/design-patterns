from typing import Optional


class Computer:
    def __init__(self) -> None:
        self.cpu: Optional[str] = None
        self.ram: Optional[int] = None
        self.storage: Optional[int] = None
        self.gpu: Optional[str] = None
        self.power_supply: Optional[int] = None

    def __str__(self) -> str:
        cpu_str = self.cpu if self.cpu else "Not specified"
        ram_str = f"{self.ram} GB" if self.ram is not None else "Not specified"
        storage_str = (
            f"{self.storage} GB" if self.storage is not None else "Not specified"
        )
        gpu_str = self.gpu if self.gpu else "Not specified"
        psu_str = (
            f"{self.power_supply}W"
            if self.power_supply is not None
            else "Not specified"
        )

        return (
            f"Computer Configuration:\n"
            f"  - CPU:          {cpu_str}\n"
            f"  - RAM:          {ram_str}\n"
            f"  - Storage:      {storage_str}\n"
            f"  - GPU:          {gpu_str}\n"
            f"  - Power Supply: {psu_str}\n"
        )
