# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-23

### Ajouté
- Script principal `timecode_extractor.py` pour l'extraction et modification de timecode
- Support de multiples formats de noms de fichiers de drones :
  - Format DJI standard (`DJI_0001_143025.MP4`)
  - Format DJI avec date complète (`DJI_20250522223921_0094_D.MP4`)
  - Format DRONE avec date (`DRONE_20240610_091530.mov`)
  - Format VID (`VID_143045_001.MP4`)
  - Formats avec tirets et points
- Traitement par lot de dossiers entiers
- Sauvegarde automatique des fichiers originaux
- Interface en ligne de commande avec options avancées
- Support de multiples formats vidéo (MP4, MOV, AVI, MKV, etc.)
- Fichier de configuration `config.py` pour personnalisation
- Tests unitaires complets
- Exemples d'utilisation détaillés
- Script batch pour Windows (glisser-déposer)
- Documentation complète avec guides d'utilisation
- Support des framerates personnalisés
- Validation des valeurs temporelles
- Gestion d'erreurs robuste

### Fonctionnalités techniques
- Extraction via expressions régulières
- Modification des métadonnées FFmpeg sans réencodage
- Validation des chemins et extensions
- Interface utilisateur claire avec emojis
- Support des environnements virtuels Python

## [Unreleased]

### Prévu
- Interface graphique (GUI) optionnelle
- Support de formats de noms additionnels
- Export des rapports de traitement
- Mode de traitement parallèle pour de gros volumes
- Détection automatique des framerates
