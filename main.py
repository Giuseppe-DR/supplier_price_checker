from db.sqlite_utils import create_database, insert_items
from parsers.cedi_parser import parse_row_pair_csv
from utils.pdf_to_csv import convert_pdf_to_csv
from utils.clean_csv import filter_csv_by_keywords

#pdf_path = ("C:\\Users\\Giuseppe\\Desktop\\singlePage.pdf")
#csv_path = convert_pdf_to_csv(pdf_path)
#filter_csv_by_keywords(csv_path,csv_path)
items = parse_row_pair_csv("data/converted_csv/singlePage.csv", supplier="CEDI")
db_path = "data/items.db"
create_database(db_path)
insert_items(items, db_path)