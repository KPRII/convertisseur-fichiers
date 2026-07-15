from pathlib import Path
from pypdf import PdfWriter

def merge_pdfs(input_paths: list[Path], output_path: Path):
    writer = PdfWriter()
    for path in input_paths:
        writer.append(path)
    writer.write(output_path)