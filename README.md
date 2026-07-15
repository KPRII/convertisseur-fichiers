# Convertisseur de fichiers

Un outil en ligne de commande simple pour convertir des fichiers, sans dépendre d'un site web louche qui upload tes fichiers sur un serveur inconnu. Tout se passe en local, sur ta machine.

## Fonctionnalités

- **Images** : conversion entre formats (PNG, JPG, WebP...)
- **PDF** : fusion de plusieurs fichiers en un seul
- **Audio** : conversion entre formats (MP3, WAV, OGG, FLAC)

## Installation

```bash
git clone https://github.com/KPRII/convertisseur-fichiers.git
cd convertisseur-fichiers
pip install -r requirements.txt
```

Nécessite aussi [ffmpeg](https://ffmpeg.org/) installé sur le système pour la conversion audio.

## Utilisation

```bash
# Convertir une image
python main.py photo.png photo.jpg

# Fusionner des PDF
python main.py doc1.pdf doc2.pdf fusion.pdf

# Convertir un fichier audio
python main.py musique.mp3 musique.wav
```