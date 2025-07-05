from utils.pdf_reader import extract_text_lines
from parsers.CediParser import parse_supplier_grid_style

pdf_path = "C:\\Users\\Giuseppe\\Desktop\\TryNullParam.pdf"  # Replace with your PDF path
lines = extract_text_lines(pdf_path)
for idx, line in enumerate(lines):
    print(f"{idx:03}: {line}")
items = parse_supplier_grid_style(lines)
for item in items:
    print(item)