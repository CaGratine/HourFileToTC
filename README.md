# HeureFichierToTC - Extracteur de Timecode depuis les Noms de Fichiers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

Script Python pour extraire l'heure des noms de fichiers vidéo de drone et modifier les métadonnées de timecode pour faciliter la synchronisation en post-production.

## 🎯 Problématique

Les rushes de drone n'ont souvent pas de son et utilisent un timecode qui ne correspond pas aux autres caméras du tournage. Cependant, le nom de fichier contient généralement l'heure de création du fichier, ce qui peut servir de référence pour la synchronisation.

## ✨ Fonctionnalités

- ✅ **Extraction automatique** de l'heure depuis les noms de fichiers
- ✅ **Support de multiples formats** de drones (DJI, etc.)
- ✅ **Conversion en format timecode** (HH:MM:SS:FF)
- ✅ **Traitement par lot** de dossiers entiers
- ✅ **Sauvegarde automatique** des fichiers originaux
- ✅ **Configuration flexible** des patterns
- ✅ **Interface en ligne de commande** simple

## 🚀 Installation

### Prérequis
- Python 3.7 ou plus récent
- FFmpeg installé et accessible dans le PATH

### Installation rapide
```bash
git clone https://github.com/CaGratine/HourFileToTC.git
cd HourFileToTC
pip install -r requirements.txt
```

### 🍎 Installation macOS/Linux
Consultez le [guide spécifique macOS/Linux](README_MACOS_LINUX.md) pour l'installation sur ces plateformes.

## 📖 Utilisation

### Ligne de commande

```bash
# Traiter un seul fichier
python timecode_extractor.py "DJI_0001_143025.MP4"

# Traiter un dossier entier
python timecode_extractor.py "C:\Mes_Rushes_Drone"

# Avec dossier de sortie séparé
python timecode_extractor.py "C:\Rushes" -o "C:\Rushes_Traites"

# Sans sauvegarde des originaux
python timecode_extractor.py "C:\Rushes" --no-backup

# Avec framerate personnalisé (30 fps)
python timecode_extractor.py "DJI_0001_143025.MP4" -f 30
```

### Glisser-déposer (Windows)
1. Glissez votre fichier/dossier sur `timecode_batch.bat`
2. Le script s'exécute automatiquement

## 🎬 Formats de noms supportés

| Format | Exemple | Heure extraite |
|--------|---------|----------------|
| DJI Standard | `DJI_0001_143025.MP4` | 14:30:25 |
| DJI Complet | `DJI_20250522223921_0094_D.MP4` | 22:39:21 |
| DRONE avec date | `DRONE_20240610_091530.mov` | 09:15:30 |
| Format VID | `VID_143045_001.MP4` | 14:30:45 |
| Avec tirets | `drone-14-30-25.mov` | 14:30:25 |
| Avec points | `aerial.14.30.25.mkv` | 14:30:25 |

## 🎥 Formats vidéo supportés

MP4, MOV, AVI, MKV, M4V, WMV, FLV, WEBM

## 📋 Exemples d'utilisation

```bash
# Afficher l'aide
python timecode_extractor.py --help

```

## 🔧 Configuration

Vous pouvez personnaliser les patterns dans `config.py` pour vos besoins spécifiques.

## 🎞️ Intégration workflow

1. **📁** Organiser les rushes de drone dans un dossier dédié
2. **🏃** Exécuter le script sur le dossier entier
3. **📤** Importer les fichiers traités (suffixe '_tc') dans votre logiciel de montage
4. **🎬** Les timecodes correspondent maintenant approximativement à l'heure de tournage
5. **🔧** Ajuster finement la synchronisation si nécessaire

## 📚 Documentation

- [Guide d'utilisation détaillé](GUIDE_UTILISATION.md)
- [Exemples d'utilisation](examples.py)
- [Tests](test_extractor.py)

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commiter vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pusher vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## ⚠️ Avertissement

- Gardez toujours une copie de sauvegarde de vos rushes originaux
- Vérifiez que l'heure de votre drone était correctement réglée lors du tournage
- Ce script fournit une synchronisation approximative, un ajustement manuel peut être nécessaire
- Testez d'abord sur quelques fichiers avant de traiter l'ensemble de vos rushes

## 🐛 Support

En cas de problème :
1. Vérifiez que Python est installé : `python --version`
2. Vérifiez que FFmpeg est installé : `ffmpeg -version`
3. Installez les dépendances : `pip install -r requirements.txt`
4. Consultez les [Issues](https://github.com/CaGratine/HourFileToTC/issues)

---

**⭐ Si ce projet vous aide, n'hésitez pas à lui donner une étoile !**
