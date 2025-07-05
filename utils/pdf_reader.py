import pdfplumber

def extract_text_lines(pdf_path, skip_keywords=None):
    if skip_keywords is None:
        skip_keywords = ["Promo", "Articolo","Descrizione","Lista","Brand", "Prezzo"]

    lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    # Only keep lines that do NOT contain any of the skip keywords
                    if not any(keyword.lower() in line.lower() for keyword in skip_keywords):
                        lines.append(line)
    return lines
