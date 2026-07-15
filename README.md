# Convertisseur de fichiers

Un outil en ligne de commande simple pour convertir des fichiers, sans dépendre d'un site web louche qui upload tes fichiers sur un serveur inconnu. Tout se passe en local, sur ta machine.

## Fonctionnalités

- **Images** : conversion entre formats (PNG, JPG, WebP...)
- **PDF** : fusion de plusieurs fichiers en un seul
- **Audio** : conversion entre formats (MP3, WAV, OGG, FLAC)
- **Vidéo** : conversion entre formats (MP4, AVI, MOV, MKV)
- **Dossier entier** : convertit tous les fichiers d'un dossier d'un coup
- **application graphique** : une application pour les personne en difficulté

## Installation

```bash
git clone https://github.com/KPRII/convertisseur-fichiers.git
cd convertisseur-fichiers
pip install -r requirements.txt
```

Nécessite aussi [ffmpeg](https://ffmpeg.org/) installé sur le système (pour l'audio et la vidéo).

## Utilisation

```bash
# Convertir une image
python main.py photo.png photo.jpg

# Fusionner des PDF
python main.py doc1.pdf doc2.pdf fusion.pdf

# Convertir un fichier audio
python main.py musique.mp3 musique.wav

# Convertir une vidéo
python main.py video.mp4 video.avi

# Convertir tous les fichiers d'un dossier
python main.py mon_dossier --format jpg
```

## Licence

MIT
