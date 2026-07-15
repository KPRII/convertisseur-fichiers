import argparse
from pathlib import Path
from images import convert_image
from pdfs import merge_pdfs
from audio import convert_audio

def main():
    parser = argparse.ArgumentParser(description="Convertisseur de fichiers")
    parser.add_argument("inputs", nargs="+", help="Fichier(s) a traiter")
    parser.add_argument("output", help="Fichier de sortie")
    args = parser.parse_args()

    input_paths = [Path(p) for p in args.inputs]
    output_path = Path(args.output)

    for path in input_paths:
        if not path.exists():
            print(f"Erreur : le fichier '{path}' n'existe pas.")
            return

    audio_extensions = {".mp3", ".wav", ".ogg", ".flac"}
    all_pdfs = all(p.suffix.lower() == ".pdf" for p in input_paths)

    try:
        if output_path.suffix.lower() == ".pdf" and all_pdfs:
            merge_pdfs(input_paths, output_path)
        elif input_paths[0].suffix.lower() in audio_extensions:
            convert_audio(input_paths[0], output_path)
        else:
            convert_image(input_paths[0], output_path)
        print(f"Conversion reussie : {output_path}")
    except Exception as e:
        print(f"Erreur pendant la conversion : {e}")

if __name__ == "__main__":
    main()