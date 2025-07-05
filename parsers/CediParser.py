def parse_supplier_grid_style(lines):
    items = []
    i = 0
    while i < len(lines) - 1:
        # Row 1: Code + Description
        row1 = lines[i].strip().split()

        # Row 2: U.M + Quantities + Price + Codice a barre (last)
        row2 = lines[i + 1].strip().split()

        # Remove last column if present (Codice a barre)
        if len(row2) > 9:
            row2 = row2[:9]  # keep only columns A–I (indices 0–8)

        # Skip malformed lines
        if len(row1) < 2 or len(row2) < 5:
            i += 1
            continue

        try:
            # === From Row 1 ===
            code = row1[0]                      # Column A
            description = " ".join(row1[1:])    # Columns B–D

            # === From Row 2 ===
            unit = row2[0]                      # Column B
            print(row2[4])
            price = float(row2[4])              # Column E (Prezzo Netto)

        except ValueError:
            price = None

        item = {
            "supplier": "CEDI",
            "code": code,
            "description": description,
            "unit": unit,
            "price": price
        }

        items.append(item)
        i += 2

    return items
