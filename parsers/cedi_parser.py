import csv
from models.item_dto import ItemDTO


def parse_row_pair_csv(csv_path: str, supplier: str) -> list[ItemDTO]:
    items = []

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))

        for i in range(0, len(reader), 2):  # Step by 2: pairs of rows
            if i + 1 >= len(reader):
                break  # Prevent index out of range

            row1 = reader[i]
            row2 = reader[i + 1]

            article_code = row1[0].strip()
            supplier_code = row2[0].strip()
            description = row1[1].strip()
            price_str = row2[2].replace(",", ".").strip()
            cont_cfz_str = row2[3].strip()

            try:
                price = float(price_str)
                quantity =  int(float(cont_cfz_str.replace(",",".")))
            except ValueError:
                continue  # Skip malformed rows

            item = ItemDTO(
                supplier = supplier,
                articleCode = article_code,
                supplierCode =supplier_code,
                description = description,
                price = price,
                quantity = quantity
            )
            items.append(item)
    return items
