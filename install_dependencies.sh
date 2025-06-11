#!/bin/bash
# Script d'installation automatique des dépendances
# pour HeureFichierToTC sur macOS/Linux

echo "=========================================="
echo " INSTALLATION DES DEPENDANCES"
echo "=========================================="
echo

echo "Vérification de Python..."
if command -v python3 &> /dev/null; then
    python3 --version
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    python --version
    PYTHON_CMD="python"
else
    echo "ERREUR: Python n'est pas installé ou pas dans le PATH"
    echo "Veuillez installer Python depuis https://python.org"
    echo "Ou via Homebrew: brew install python3"
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

echo
echo "Vérification de FFmpeg..."
if command -v ffmpeg &> /dev/null; then
    echo "FFmpeg trouvé: $(ffmpeg -version 2>&1 | head -n 1)"
else
    echo "AVERTISSEMENT: FFmpeg n'est pas installé ou pas dans le PATH"
    echo "Le script pourra extraire les heures mais ne pourra pas modifier les métadonnées"
    echo
    echo "Pour installer FFmpeg:"
    echo "- macOS: brew install ffmpeg"
    echo "- Ubuntu/Debian: sudo apt install ffmpeg"
    echo "- CentOS/RHEL: sudo yum install ffmpeg"
    echo
fi

echo "Installation des dépendances Python..."

# Vérifier si pip est disponible
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
else
    echo "ERREUR: pip n'est pas installé"
    echo "Installez pip avec: $PYTHON_CMD -m ensurepip --upgrade"
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

# Installation des dépendances
$PIP_CMD install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERREUR: Échec de l'installation des dépendances"
    echo "Essayez avec --user: $PIP_CMD install --user -r requirements.txt"
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

echo
echo "=========================================="
echo "Installation terminée avec succès !"
echo "=========================================="
echo
echo "Vous pouvez maintenant utiliser le script :"
echo "$PYTHON_CMD timecode_extractor.py \"votre_fichier.mp4\""
echo
echo "Ou utilisez ./timecode_script.sh pour le glisser-déposer"
echo "N'oubliez pas de rendre le script exécutable avec:"
echo "chmod +x timecode_script.sh"
echo
read -p "Appuyez sur Entrée pour continuer..."
