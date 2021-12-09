from dataclasses import dataclass


@dataclass
class Cargo:
    id: str
    description: str
    amount: int
    weight: float
    length: float
    width: float
    height: float
