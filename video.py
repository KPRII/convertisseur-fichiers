import subprocess
from pathlib import Path

def convert_video(input_path: Path, output_path: Path):
    subprocess.run(
        ["ffmpeg", "-i", str(input_path), str(output_path), "-y"],
        check=True
    )

def extract_audio(input_path: Path, output_path: Path):
    subprocess.run(
        ["ffmpeg", "-i", str(input_path), "-vn", str(output_path), "-y"],
        check=True
    )