import csv
from models.item_dto import ItemDTO


def parse_row_pair_csv(csv_path: str, supplier: str) -> list[ItemDTO]:
    items = []

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))

        for i in range(0, len(reader), 2):  # Step by 2: pair of rows
            if i + 1 >= len(reader):
                break  # Prevent index out of range

            row1 = reader[i]
            row2 = reader[i + 1]

            articleCode = row1[0].strip()
            supplierCode = row2[0].strip()
            description = row1[1].strip()
            price_str = row2[2].replace(",", ".").strip()


            try:
                price = float(price_str)
            except ValueError:
                continue  # Skip malformed rows

            item = ItemDTO(
                supplier = supplier,
                articleCode = articleCode,
                supplierCode =supplierCode,
                description = description,
                price = price
            )
            items.append(item)

    return items
