from dataclasses import dataclass

@dataclass
class ItemDTO:
    supplier: str
    code: str
    description: str
    unit: str
    price: float
