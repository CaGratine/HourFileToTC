@echo off
:: Script batch pour utiliser facilement l'extracteur de timecode
:: Usage: Glisser-déposer un fichier ou dossier sur ce script

echo ========================================
echo  EXTRACTEUR DE TIMECODE - RUSHES DRONE
echo ========================================
echo.

if "%~1"=="" (
    echo Erreur: Aucun fichier ou dossier specifie
    echo.
    echo Usage: Glissez-deposez un fichier video ou un dossier sur ce script
    echo Ou utilisez: timecode_batch.bat "chemin_vers_fichier_ou_dossier"
    echo.
    pause
    exit /b 1
)

echo Traitement de: %~1
echo.

:: Exécution du script Python
python "%~dp0timecode_extractor.py" "%~1"

echo.
echo ========================================
echo Traitement termine !
echo ========================================
pause
