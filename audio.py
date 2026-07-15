from pathlib import Path
from pydub import AudioSegment

def convert_audio(input_path: Path, output_path: Path):
    audio = AudioSegment.from_file(input_path)
    output_format = output_path.suffix.lstrip(".")
    audio.export(output_path, format=output_format)