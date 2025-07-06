import tabula
import os

def convert_pdf_to_csv(pdf_path: str, output_dir: str = "data/converted_csv", pages: str = "all") -> str:
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define output path
    output_csv_path = os.path.join(output_dir, os.path.basename(pdf_path).replace(".pdf", ".csv"))

    # Extract tables and write to CSV
    tabula.convert_into(
        input_path=pdf_path,
        output_path=output_csv_path,
        output_format="csv",
        pages=pages,
        lattice=True  # lattice=True works well with grid-style PDFs
    )
    print(f"✅ CSV created at: {output_csv_path}")
    return output_csv_path
