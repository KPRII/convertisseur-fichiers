from pathlib import Path
from pypdf import PdfWriter
from PIL import Image

def merge_pdfs(input_paths: list[Path], output_path: Path):
    writer = PdfWriter()
    for path in input_paths:
        writer.append(path)
    writer.write(output_path)

def images_to_pdf(input_paths: list[Path], output_path: Path):
    images = [Image.open(p).convert("RGB") for p in input_paths]
    first_image, rest = images[0], images[1:]
    first_image.save(output_path, save_all=True, append_images=rest)

def pdf_to_images(input_path: Path, output_folder: Path):
    from pypdf import PdfReader
    reader = PdfReader(input_path)
    output_folder.mkdir(exist_ok=True)
    for i, page in enumerate(reader.pages):
        for image in page.images:
            out_path = output_folder / f"page_{i+1}_{image.name}"
            with open(out_path, "wb") as f:
                f.write(image.data)