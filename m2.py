from db.sqlite_utils import create_database, insert_items, search_items_by_name
from parsers.cedi_parser import parse_row_pair_csv
from utils.pdf_to_csv import convert_pdf_to_csv
from utils.clean_csv import filter_csv_by_keywords

#pdf_path = ("C:\\Users\\Giuseppe\\Desktop\\singlePage.pdf")
#csv_path = convert_pdf_to_csv(pdf_path)
#filter_csv_by_keywords(csv_path,csv_path)
#items = parse_row_pair_csv("data/converted_csv/singlePage.csv", supplier="CEDI")
db_path = "data/items.db"
#create_database(db_path)
#insert_items(items, db_path)
query = input("🔍 Enter product name or article code to search: ")
results = search_items_by_name(query, db_path="data/items.db")
if results:
    print(f"\nFound {len(results)} matching items:\n")
    for item in results:
        print(f"🔹 {item.supplier} | {item.articleCode} | {item.supplierCode} |  {item.description} |  €{item.price:.4f}")
else:
    print("❌ No matching items found.")