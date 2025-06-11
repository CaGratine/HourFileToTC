# 🍎 Guide d'installation et d'utilisation - macOS/Linux

## 🚀 Installation rapide

### macOS avec Homebrew (recommandé)
```bash
# 1. Téléchargez le projet
git clone https://github.com/CaGratine/HourFileToTC.git
cd HourFileToTC

# 2. Exécutez l'installation automatique
chmod +x install_macos.sh
./install_macos.sh
```

### Linux (Ubuntu/Debian)
```bash
# 1. Installez les dépendances système
sudo apt update
sudo apt install python3 python3-pip ffmpeg

# 2. Téléchargez le projet
git clone https://github.com/CaGratine/HourFileToTC.git
cd HourFileToTC

# 3. Installez les dépendances Python
chmod +x install_dependencies.sh
./install_dependencies.sh
```

### Linux (CentOS/RHEL)
```bash
# 1. Installez les dépendances système
sudo yum install python3 python3-pip ffmpeg

# 2. Téléchargez le projet et installez
git clone https://github.com/CaGratine/HourFileToTC.git
cd HourFileToTC
chmod +x install_dependencies.sh
./install_dependencies.sh
```

## 💻 Utilisation

### Ligne de commande
```bash
# Traiter un fichier
python3 timecode_extractor.py "DJI_0001_143025.MP4"

# Traiter un dossier
python3 timecode_extractor.py "/Users/nom/Videos/Drone"

# Avec options
python3 timecode_extractor.py "fichier.mp4" -o "/Users/nom/Output" -f 30
```

### Script shell (équivalent du .bat Windows)
```bash
# Rendre le script exécutable
chmod +x timecode_script.sh

# Utiliser le script
./timecode_script.sh "DJI_0001_143025.MP4"
```

### Glisser-déposer (macOS)
1. Ouvrez le Terminal
2. Tapez `./timecode_script.sh ` (avec un espace à la fin)
3. Glissez votre fichier/dossier vidéo dans le Terminal
4. Appuyez sur Entrée

## 🔧 Dépannage

### "Permission denied"
```bash
chmod +x *.sh
```

### "python3: command not found"
```bash
# macOS
brew install python

# Ubuntu/Debian
sudo apt install python3

# CentOS/RHEL
sudo yum install python3
```

### "ffmpeg: command not found"
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg
```

### Problèmes de dépendances Python
```bash
# Installation avec --user
pip3 install --user -r requirements.txt

# Ou avec sudo (non recommandé)
sudo pip3 install -r requirements.txt
```

## 📋 Différences avec Windows

| Windows | macOS/Linux | Description |
|---------|-------------|-------------|
| `timecode_batch.bat` | `timecode_script.sh` | Script de glisser-déposer |
| `install_dependencies.bat` | `install_dependencies.sh` | Installation dépendances |
| `python` | `python3` | Commande Python |
| `pip` | `pip3` | Gestionnaire de paquets |

## 🍎 Spécificités macOS

- **Homebrew** recommandé pour l'installation
- **Gatekeeper** peut bloquer les scripts : `System Preferences > Security & Privacy`
- **Terminal** accessible via `Cmd + Space` puis taper "Terminal"

## 🐧 Spécificités Linux

- **Gestionnaire de paquets** varie selon la distribution
- **Permissions** importantes pour les scripts shell
- **FFmpeg** disponible dans la plupart des dépôts

## ❓ Support

Pour obtenir de l'aide :
1. Consultez les [Issues GitHub](https://github.com/CaGratine/HourFileToTC/issues)
2. Vérifiez le [guide principal](README.md)
3. Ouvrez une nouvelle issue si nécessaire
