def parse_supplier_grid_style(lines):
    items = []
    i = 0
    while i < len(lines) -1:
        # Row 1 are formatted like this [Cod.Articolo, Descrizione]
        # Row 2 are formatted like this [Cod.Fornitore, PZ, Prezzo, ContCfz, Strato, Pallet]
        row1 = lines[i].strip().split()
        row1 = row1[:-1]  # Remove Codice a barre
        print("row1: ",row1)
        # Row 2: U.M + Quantities + Price + Codice a barre (last)
        row2 = lines[i + 1].strip().split()
        print("row2: ",row2)
        print(len(row2))
        # Skip malformed lines
        if len(row1) <= 1 or len(row2) <= 1:
            i += 1
            continue

        try:
            # === From Row 1 ===
            articleCode = row1[0]
            description = " ".join(row1[1:])

            # === From Row 2 ===
            if len(row2) > 5:
                supplyerCode = row2[0]
                price = float(row2[2])
                contCfz = row2[3]
                strato: row2[4]
                pallet: row2[5]
            else:
                supplyerCode = "NP"
                price = float(row2[1])
                contCfz = row2[2]
                strato: row2[3]
                pallet: row2[4]


        except ValueError:
            price = None

        item = {
            "supplier": "CEDI",
            "articleCode": articleCode,
            "description": description,
            "supplyerCode": supplyerCode,
            "price": price,
            "contCfz": contCfz
        }

        items.append(item)
        i += 2
    return items
