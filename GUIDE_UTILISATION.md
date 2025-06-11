# GUIDE D'UTILISATION - Extracteur de Timecode

## 🚀 Utilisation rapide en ligne de commande

### Prérequis
- Python installé sur votre système
- FFmpeg installé et accessible dans le PATH
- Dépendances installées : `pip install -r requirements.txt`

### Syntaxe de base
```
python timecode_extractor.py [fichier_ou_dossier] [options]
```

### Exemples concrets

#### 1. Traiter un seul fichier
```bash
python timecode_extractor.py "DJI_0001_143025.MP4"
```
**Résultat :** Crée `DJI_0001_143025_tc.MP4` avec timecode 14:30:25:00

#### 2. Traiter tout un dossier
```bash
python timecode_extractor.py "C:\Mes_Rushes_Drone"
```
**Résultat :** Traite tous les fichiers vidéo du dossier

#### 3. Avec dossier de sortie séparé
```bash
python timecode_extractor.py "C:\Rushes" -o "C:\Rushes_Traites"
```
**Résultat :** Sauvegarde les fichiers traités dans un autre dossier

#### 4. Sans créer de sauvegarde
```bash
python timecode_extractor.py "C:\Rushes" --no-backup
```
**Résultat :** Ne garde pas de copie des fichiers originaux

#### 5. Avec framerate personnalisé
```bash
python timecode_extractor.py "DJI_0001_143025.MP4" -f 30
```
**Résultat :** Utilise 30 fps au lieu de 25 fps par défaut

### Options disponibles
- `-o, --output` : Dossier de sortie
- `-f, --framerate` : Framerate (défaut: 25 fps)
- `--no-backup` : Ne pas créer de sauvegarde
- `-h, --help` : Afficher l'aide

### Formats de noms supportés
- `DJI_0001_143025.MP4` → 14:30:25
- `DJI_20250522223921_0094_D.MP4` → 22:39:21
- `DRONE_20240610_091530.mov` → 09:15:30
- `VID_143045_001.MP4` → 14:30:45
- `drone-14-30-25.mov` → 14:30:25
- `aerial.14.30.25.mkv` → 14:30:25

### Utilisation par glisser-déposer (Windows)
1. Double-cliquez sur `timecode_batch.bat`
2. Ou glissez-déposez un fichier/dossier sur `timecode_batch.bat`

### Extensions vidéo supportées
MP4, MOV, AVI, MKV, M4V, WMV, FLV, WEBM

### En cas de problème
1. Vérifiez que Python est installé : `python --version`
2. Vérifiez que FFmpeg est installé : `ffmpeg -version`
3. Installez les dépendances : `pip install -r requirements.txt`
4. Consultez l'aide : `python timecode_extractor.py --help`
