import argparse
from pathlib import Path
from images import convert_image
from pdfs import merge_pdfs, images_to_pdf, pdf_to_images
from audio import convert_audio
from video import convert_video, extract_audio

AUDIO_EXTENSIONS = {".mp3", ".wav", ".ogg", ".flac"}
VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}

def convert_one(input_path: Path, output_path: Path):
    suffix = input_path.suffix.lower()
    if suffix in VIDEO_EXTENSIONS:
        convert_video(input_path, output_path)
    elif suffix in AUDIO_EXTENSIONS:
        convert_audio(input_path, output_path)
    else:
        convert_image(input_path, output_path)

def process_folder(folder: Path, target_format: str):
    for file in folder.iterdir():
        if file.is_file():
            output_path = file.with_suffix(f".{target_format}")
            try:
                convert_one(file, output_path)
                print(f"Conversion reussie : {output_path}")
            except Exception as e:
                print(f"Erreur sur {file.name} : {e}")

def main():
    parser = argparse.ArgumentParser(description="Convertisseur de fichiers")
    parser.add_argument("inputs", nargs="+", help="Fichier(s) d'entree, puis fichier de sortie (ou un dossier seul avec --format)")
    parser.add_argument("--format", help="Format cible pour un dossier entier (ex: jpg, mp3)")
    args = parser.parse_args()

    first_input = Path(args.inputs[0])

    if len(args.inputs) == 1 and first_input.is_dir():
        if not args.format:
            print("Erreur : precise --format quand tu traites un dossier (ex: --format jpg)")
            return
        process_folder(first_input, args.format)
        return

    input_paths = [Path(p) for p in args.inputs[:-1]]
    output_path = Path(args.inputs[-1])

    for path in input_paths:
        if not path.exists():
            print(f"Erreur : le fichier '{path}' n'existe pas.")
            return

    all_pdfs = all(p.suffix.lower() == ".pdf" for p in input_paths)
    all_images = all(p.suffix.lower() in IMAGE_EXTENSIONS for p in input_paths)

    try:
        if output_path.suffix.lower() == ".pdf" and all_pdfs:
            merge_pdfs(input_paths, output_path)
        elif output_path.suffix.lower() == ".pdf" and all_images:
            images_to_pdf(input_paths, output_path)
        elif input_paths[0].suffix.lower() == ".pdf" and output_path.suffix.lower() == "":
            pdf_to_images(input_paths[0], output_path)
        elif input_paths[0].suffix.lower() in VIDEO_EXTENSIONS and output_path.suffix.lower() in AUDIO_EXTENSIONS:
            extract_audio(input_paths[0], output_path)
        else:
            convert_one(input_paths[0], output_path)
        print(f"Conversion reussie : {output_path}")
    except Exception as e:
        print(f"Erreur pendant la conversion : {e}")

if __name__ == "__main__":
    main()