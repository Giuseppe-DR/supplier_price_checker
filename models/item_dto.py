from dataclasses import dataclass

@dataclass
class ItemDTO:
    supplier: str
    articleCode: str
    supplierCode: str
    description: str
    price: float
    quantity: int
    ean: str = ""
    netto: float = 0.0
    ivato: float = 0.0