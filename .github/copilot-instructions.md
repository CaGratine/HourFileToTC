<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Instructions spécifiques pour le projet HeureFichierToTC

Ce projet est un script Python pour extraire l'heure des noms de fichiers vidéo de drone et modifier les métadonnées de timecode pour faciliter la synchronisation en post-production.

## Contexte du projet
- Les rushes de drone n'ont pas de son et ont un timecode qui ne correspond pas aux autres caméras
- Le nom de fichier contient l'heure de création qui peut servir pour la synchronisation
- L'objectif est d'automatiser l'extraction de cette heure et la mise à jour des métadonnées

## Technologies utilisées
- Python 3.x
- ffmpeg-python pour la manipulation des métadonnées vidéo
- regex pour l'extraction des patterns d'heure dans les noms de fichiers
- pathlib pour la gestion des chemins de fichiers

## Fonctionnalités principales
1. Lire les noms de fichiers vidéo
2. Extraire l'heure contenue dans le nom (différents formats possibles)
3. Convertir en format timecode (HH:MM:SS:FF)
4. Modifier les métadonnées de start timecode du fichier vidéo
