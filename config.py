"""
Configuration pour l'extracteur de timecode.

Ce fichier permet de personnaliser les patterns de reconnaissance
et les paramètres du script selon vos besoins spécifiques.
"""

# Patterns personnalisés pour l'extraction d'heure
# Format: (nom_du_pattern, regex, description)
CUSTOM_TIME_PATTERNS = [
    # Ajoutez vos propres patterns ici
    # Exemple: ("mon_drone", r'MYDRONE_(\d{2})(\d{2})(\d{2})', "Mon format de drone spécifique")
]

# Extensions vidéo supplémentaires à traiter
ADDITIONAL_VIDEO_EXTENSIONS = [
    # Ajoutez d'autres extensions si nécessaire
    # Exemple: '.mts', '.m2ts'
]

# Framerate par défaut pour différents types de drones
DRONE_FRAMERATES = {
    'dji': 30.0,
    'gopro': 60.0,
    'default': 25.0
}

# Configuration des métadonnées
METADATA_CONFIG = {
    # Préfixe pour les fichiers de sortie
    'output_suffix': '_tc',
    
    # Préfixe pour les sauvegardes
    'backup_suffix': '_backup',
    
    # Métadonnées supplémentaires à ajouter
    'additional_metadata': {
        # 'artist': 'Votre nom',
        # 'comment': 'Timecode extrait automatiquement'
    }
}

# Messages personnalisés
MESSAGES = {
    'processing': 'Traitement en cours...',
    'success': 'Fichier traité avec succès',
    'error': 'Erreur lors du traitement',
    'no_pattern': 'Aucun pattern d\'heure trouvé'
}
