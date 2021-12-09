from dataclasses import dataclass
from core.models.cargo import Cargo


@dataclass
class CargoRequest:
    id: str
    cargo: Cargo
