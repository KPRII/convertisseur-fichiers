from pathlib import Path
from PIL import Image

def convert_image(input_path: Path, output_path: Path):
    image = Image.open(input_path)
    image.save(output_path)