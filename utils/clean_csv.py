import csv
import os

def filter_csv_by_keywords(input_path, output_path):

    skip_keywords = ["Promo", "Articolo","Descrizione","Lista","Brand", "Prezzo"]

    # Ensure parent folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cleaned_rows = []

    with open(input_path, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if not any(row):
                continue

            row_text = " ".join(row).lower()
            if any(kw.lower() in row_text for kw in skip_keywords):
                continue


            if len(row) == 1:
                continue

            cleaned_rows.append(row)

    with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)

    print(f"✅ Filtered CSV saved to: {output_path}")
