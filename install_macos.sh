#!/bin/bash
# Script d'installation spécifique pour macOS
# Utilise Homebrew pour installer les dépendances

echo "=========================================="
echo " INSTALLATION MACOS - HEUREFICHIERTOTC"
echo "=========================================="
echo

# Vérifier si Homebrew est installé
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew n'est pas installé"
    echo
    echo "Installation de Homebrew..."
    echo "Copiez-collez cette commande dans le Terminal:"
    echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
    echo
    echo "Puis relancez ce script"
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

echo "✅ Homebrew détecté"
echo

# Mettre à jour Homebrew
echo "🔄 Mise à jour de Homebrew..."
brew update

# Installer Python si nécessaire
if ! command -v python3 &> /dev/null; then
    echo "📦 Installation de Python..."
    brew install python
else
    echo "✅ Python déjà installé: $(python3 --version)"
fi

# Installer FFmpeg si nécessaire
if ! command -v ffmpeg &> /dev/null; then
    echo "📦 Installation de FFmpeg..."
    brew install ffmpeg
else
    echo "✅ FFmpeg déjà installé"
fi

echo
echo "📦 Installation des dépendances Python..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Échec de l'installation des dépendances"
    echo "Essayez avec --user: pip3 install --user -r requirements.txt"
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

# Rendre les scripts exécutables
echo "🔧 Configuration des permissions..."
chmod +x timecode_script.sh
chmod +x install_dependencies.sh

echo
echo "=========================================="
echo "✅ Installation macOS terminée !"
echo "=========================================="
echo
echo "🚀 Utilisation:"
echo "   python3 timecode_extractor.py \"votre_fichier.mp4\""
echo "   ou ./timecode_script.sh \"votre_fichier.mp4\""
echo
echo "📁 Glisser-déposer:"
echo "   Faites glisser un fichier sur timecode_script.sh"
echo
read -p "Appuyez sur Entrée pour continuer..."
