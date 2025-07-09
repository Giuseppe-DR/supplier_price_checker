import pandas as pd
from models.item_dto import ItemDTO

def parse_surgelati_xls(file_path: str, supplier_name: str) -> list[ItemDTO]:
    df = pd.read_excel(file_path)

    # Clean column names (just in case)
    df.columns = [col.strip() for col in df.columns]

    items = []

    for _, row in df.iterrows():
        try:
            item = ItemDTO(
                supplier=supplier_name,
                articleCode=str(row.get("Codice", "")).strip(),
                supplierCode="",  # Not present in this file
                description=str(row.get("Descrizione", "")).strip(),
                price=float(str(row.get("Imponibile", "0")).replace(",", ".")),
                quantity=int(float(str(row.get("PZ", "0")).replace(",", ".")))
            )
            items.append(item)
        except Exception as e:
            print(f"Skipping row due to error: {e}")

    return items
