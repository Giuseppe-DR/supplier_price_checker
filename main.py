from utils.pdf_to_csv import convert_pdf_to_csv
from utils.clean_csv import filter_csv_by_keywords
pdf_path = ("C:\\Users\\Giuseppe\\Desktop\\testlastwo.pdf")
csv_path = convert_pdf_to_csv(pdf_path)
filter_csv_by_keywords(csv_path,csv_path)
