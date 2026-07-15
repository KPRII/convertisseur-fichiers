import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
from images import convert_image
from audio import convert_audio
from video import convert_video, extract_audio
from pdfs import merge_pdfs, images_to_pdf, pdf_to_images

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Convertisseur de fichiers")
app.geometry("450x350")

selected_file = {"path": None}

def choose_file():
    path = filedialog.askopenfilename(title="Choisir un fichier")
    if path:
        selected_file["path"] = Path(path)
        file_label.configure(text=f"Fichier : {selected_file['path'].name}")

def do_convert():
    if not selected_file["path"]:
        result_label.configure(text="Choisis d'abord un fichier !")
        return

    target_format = format_entry.get().strip().lstrip(".")
    if not target_format:
        result_label.configure(text="Precise un format de sortie")
        return

    input_path = selected_file["path"]
    output_path = input_path.with_suffix(f".{target_format}")

    try:
        suffix = input_path.suffix.lower()
        if suffix in {".mp4", ".avi", ".mov", ".mkv"}:
            convert_video(input_path, output_path)
        elif suffix in {".mp3", ".wav", ".ogg", ".flac"}:
            convert_audio(input_path, output_path)
        else:
            convert_image(input_path, output_path)
        result_label.configure(text=f"Reussi : {output_path.name}")
    except Exception as e:
        result_label.configure(text=f"Erreur : {e}")

title_label = ctk.CTkLabel(app, text="Convertisseur de fichiers", font=("Arial", 20))
title_label.pack(pady=20)

choose_button = ctk.CTkButton(app, text="Choisir un fichier", command=choose_file)
choose_button.pack(pady=10)

file_label = ctk.CTkLabel(app, text="Aucun fichier choisi")
file_label.pack(pady=5)

format_entry = ctk.CTkEntry(app, placeholder_text="Format de sortie (ex: jpg, mp3)")
format_entry.pack(pady=10)

convert_button = ctk.CTkButton(app, text="Convertir", command=do_convert)
convert_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

app.mainloop()
