from db.sqlite_utils import create_database
from models.item_dto import ItemDTO
from parsers.cedi_parser import parse_row_pair_csv
from utils.clean_csv import filter_csv_by_keywords
from utils.pdf_to_csv import convert_pdf_to_csv

def insert_cedi_file (csv_path, supplier) -> list[ItemDTO]:
    output_csv_path = convert_pdf_to_csv(csv_path)
    filter_csv_by_keywords(output_csv_path, output_csv_path)
    items = parse_row_pair_csv(output_csv_path, supplier)
    create_database("data/items.db")
    return items