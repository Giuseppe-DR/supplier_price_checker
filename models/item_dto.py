from dataclasses import dataclass

@dataclass
class ItemDTO:
    supplier: str
    articleCode: str
    supplierCode: str
    description: str
    price: float
