#!/bin/bash
# Script shell pour utiliser facilement l'extracteur de timecode
# Usage: ./timecode_script.sh "chemin_vers_fichier_ou_dossier"
# Ou glisser-déposer un fichier/dossier sur ce script

echo "========================================"
echo " EXTRACTEUR DE TIMECODE - RUSHES DRONE"
echo "========================================"
echo

# Vérifier si un argument a été fourni
if [ -z "$1" ]; then
    echo "Erreur: Aucun fichier ou dossier spécifié"
    echo
    echo "Usage: ./timecode_script.sh \"chemin_vers_fichier_ou_dossier\""
    echo "Ou glissez-déposez un fichier video ou un dossier sur ce script"
    echo
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

echo "Traitement de: $1"
echo

# Obtenir le répertoire du script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Exécution du script Python
python3 "$SCRIPT_DIR/timecode_extractor.py" "$1"

echo
echo "========================================"
echo "Traitement terminé !"
echo "========================================"
read -p "Appuyez sur Entrée pour continuer..."
