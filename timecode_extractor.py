#!/usr/bin/env python3
"""
Script pour extraire l'heure des noms de fichiers vidéo et modifier les métadonnées de timecode.

Ce script analyse les noms de fichiers vidéo pour extraire l'heure de création,
la convertit en format timecode (HH:MM:SS:FF) et met à jour les métadonnées
du fichier vidéo pour faciliter la synchronisation en post-production.
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Optional, Tuple, List
import ffmpeg


class TimecodeExtractor:
    """Classe principale pour l'extraction et la modification de timecode."""    # Patterns pour différents formats de noms de fichiers
    TIME_PATTERNS = [
        # Format DJI avec date complète: DJI_20250522223921_0094_D → 22:39:21
        r'DJI_\d{8}(\d{2})(\d{2})(\d{2})_',
        # Format DJI: DJI_0001_143025.MP4 → 14:30:25
        r'DJI_\d+_(\d{2})(\d{2})(\d{2})',
        # Format avec date: DRONE_20240610_091530.mov → 09:15:30
        r'DRONE_\d{8}_(\d{2})(\d{2})(\d{2})',
        # Format VID: VID_143045_001.MP4 → 14:30:45
        r'VID_(\d{2})(\d{2})(\d{2})_\d+',
        # Format générique HHMMSS: nom_143025.ext → 14:30:25
        r'_(\d{2})(\d{2})(\d{2})',
        # Format avec tirets: nom-14-30-25.ext → 14:30:25
        r'-(\d{2})-(\d{2})-(\d{2})',
        # Format avec points: nom.14.30.25.ext → 14:30:25
        r'\.(\d{2})\.(\d{2})\.(\d{2})\.',
    ]
    
    # Extensions vidéo supportées
    VIDEO_EXTENSIONS = {'.mp4', '.mov', '.avi', '.mkv', '.m4v', '.wmv', '.flv', '.webm'}
    
    def __init__(self, framerate: float = 25.0):
        """
        Initialise l'extracteur de timecode.
        
        Args:
            framerate: Framerate par défaut pour le calcul des frames (25 fps par défaut)
        """
        self.framerate = framerate
    
    def extract_time_from_filename(self, filename: str) -> Optional[Tuple[int, int, int]]:
        """
        Extrait l'heure du nom de fichier.
        
        Args:
            filename: Nom du fichier à analyser
            
        Returns:
            Tuple (heures, minutes, secondes) ou None si aucun pattern trouvé
        """
        for pattern in self.TIME_PATTERNS:
            match = re.search(pattern, filename, re.IGNORECASE)
            if match:
                hours, minutes, seconds = map(int, match.groups())
                
                # Validation des valeurs temporelles
                if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
                    return (hours, minutes, seconds)
                    
        return None
    
    def time_to_timecode(self, hours: int, minutes: int, seconds: int, frames: int = 0) -> str:
        """
        Convertit une heure en format timecode.
        
        Args:
            hours: Heures (0-23)
            minutes: Minutes (0-59)
            seconds: Secondes (0-59)
            frames: Frames (0-framerate-1)
            
        Returns:
            String au format HH:MM:SS:FF
        """
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{frames:02d}"
    
    def get_video_info(self, filepath: str) -> dict:
        """
        Récupère les informations du fichier vidéo.
        
        Args:
            filepath: Chemin vers le fichier vidéo
            
        Returns:
            Dictionnaire avec les informations vidéo
        """
        try:
            probe = ffmpeg.probe(filepath)
            video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
            return video_info
        except Exception as e:
            print(f"Erreur lors de la lecture des informations vidéo de {filepath}: {e}")
            return {}
    
    def update_timecode_metadata(self, input_path: str, output_path: str, timecode: str) -> bool:
        """
        Met à jour les métadonnées de timecode du fichier vidéo.
        
        Args:
            input_path: Chemin du fichier d'entrée
            output_path: Chemin du fichier de sortie
            timecode: Timecode au format HH:MM:SS:FF
            
        Returns:
            True si succès, False sinon
        """
        try:
            # Création de la commande ffmpeg pour mettre à jour les métadonnées
            stream = ffmpeg.input(input_path)
            stream = ffmpeg.output(
                stream,
                output_path,
                **{
                    'metadata': f'timecode={timecode}',
                    'c': 'copy'  # Copie sans réencodage
                }
            )
            
            # Exécution de la commande
            ffmpeg.run(stream, overwrite_output=True, quiet=True)
            return True
            
        except Exception as e:
            print(f"Erreur lors de la mise à jour des métadonnées de {input_path}: {e}")
            return False
    
    def process_video_file(self, filepath: str, output_dir: Optional[str] = None, backup: bool = True) -> bool:
        """
        Traite un fichier vidéo : extrait l'heure et met à jour les métadonnées.
        
        Args:
            filepath: Chemin vers le fichier vidéo
            output_dir: Dossier de sortie (optionnel)
            backup: Créer une sauvegarde du fichier original
            
        Returns:
            True si le traitement a réussi, False sinon
        """
        filepath = Path(filepath)
        filename = filepath.name
        
        print(f"Traitement de: {filename}")
        
        # Extraction de l'heure du nom de fichier
        time_info = self.extract_time_from_filename(filename)
        if not time_info:
            print(f"  ❌ Aucun pattern d'heure trouvé dans: {filename}")
            return False
        
        hours, minutes, seconds = time_info
        timecode = self.time_to_timecode(hours, minutes, seconds)
        print(f"  🕒 Heure extraite: {hours:02d}:{minutes:02d}:{seconds:02d} → Timecode: {timecode}")
        
        # Définition des chemins de sortie
        if output_dir:
            output_path = Path(output_dir) / filename
        else:
            output_path = filepath.parent / f"{filepath.stem}_tc{filepath.suffix}"
        
        # Sauvegarde si demandée
        if backup and not output_dir:
            backup_path = filepath.parent / f"{filepath.stem}_backup{filepath.suffix}"
            if not backup_path.exists():
                try:
                    filepath.rename(backup_path)
                    original_path = backup_path
                except Exception as e:
                    print(f"  ⚠️  Erreur lors de la sauvegarde: {e}")
                    original_path = filepath
            else:
                original_path = filepath
        else:
            original_path = filepath
        
        # Mise à jour des métadonnées
        success = self.update_timecode_metadata(str(original_path), str(output_path), timecode)
        
        if success:
            print(f"  ✅ Métadonnées mises à jour: {output_path.name}")
            return True
        else:
            print(f"  ❌ Échec de la mise à jour des métadonnées")
            return False
    
    def process_directory(self, directory: str, output_dir: Optional[str] = None, backup: bool = True) -> List[str]:
        """
        Traite tous les fichiers vidéo d'un dossier.
        
        Args:
            directory: Dossier contenant les fichiers vidéo
            output_dir: Dossier de sortie (optionnel)
            backup: Créer des sauvegardes des fichiers originaux
            
        Returns:
            Liste des fichiers traités avec succès
        """
        directory = Path(directory)
        if not directory.exists():
            print(f"❌ Le dossier {directory} n'existe pas")
            return []
        
        # Création du dossier de sortie si nécessaire
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        
        # Recherche des fichiers vidéo
        video_files = []
        for ext in self.VIDEO_EXTENSIONS:
            video_files.extend(directory.glob(f"*{ext}"))
            video_files.extend(directory.glob(f"*{ext.upper()}"))
        
        if not video_files:
            print(f"❌ Aucun fichier vidéo trouvé dans {directory}")
            return []
        
        print(f"📁 Traitement de {len(video_files)} fichiers vidéo dans {directory}")
        print("-" * 60)
        
        processed_files = []
        for video_file in sorted(video_files):
            if self.process_video_file(video_file, output_dir, backup):
                processed_files.append(str(video_file))
        
        print("-" * 60)
        print(f"✅ {len(processed_files)} fichiers traités avec succès")
        
        return processed_files


def main():
    """Point d'entrée principal du script."""
    parser = argparse.ArgumentParser(
        description="Extrait l'heure des noms de fichiers vidéo et met à jour les métadonnées de timecode"
    )
    parser.add_argument(
        "path",
        help="Chemin vers un fichier vidéo ou un dossier contenant des fichiers vidéo"
    )
    parser.add_argument(
        "-o", "--output",
        help="Dossier de sortie (optionnel, sinon créé dans le même dossier)"
    )
    parser.add_argument(
        "-f", "--framerate",
        type=float,
        default=25.0,
        help="Framerate pour le calcul des frames (défaut: 25 fps)"
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Ne pas créer de sauvegarde des fichiers originaux"
    )
    
    args = parser.parse_args()
    
    # Vérification de l'existence de ffmpeg
    try:
        ffmpeg.probe("test")
    except ffmpeg.Error:
        pass  # Normal si le fichier test n'existe pas
    except FileNotFoundError:
        print("❌ FFmpeg n'est pas installé ou n'est pas dans le PATH")
        print("   Veuillez installer FFmpeg: https://ffmpeg.org/download.html")
        sys.exit(1)
    
    # Initialisation de l'extracteur
    extractor = TimecodeExtractor(framerate=args.framerate)
    
    input_path = Path(args.path)
    
    # Traitement selon le type d'entrée
    if input_path.is_file():
        # Traitement d'un fichier unique
        if input_path.suffix.lower() in extractor.VIDEO_EXTENSIONS:
            success = extractor.process_video_file(
                str(input_path),
                args.output,
                not args.no_backup
            )
            sys.exit(0 if success else 1)
        else:
            print(f"❌ {input_path} n'est pas un fichier vidéo supporté")
            sys.exit(1)
    
    elif input_path.is_dir():
        # Traitement d'un dossier
        processed = extractor.process_directory(
            str(input_path),
            args.output,
            not args.no_backup
        )
        sys.exit(0 if processed else 1)
    
    else:
        print(f"❌ Le chemin {input_path} n'existe pas")
        sys.exit(1)


if __name__ == "__main__":
    main()
