@echo off
:: Script d'installation automatique des dépendances
:: pour HeureFichierToTC

echo ==========================================
echo  INSTALLATION DES DEPENDANCES
echo ==========================================
echo.

echo Verification de Python...
python --version
if %errorlevel% neq 0 (
    echo ERREUR: Python n'est pas installe ou pas dans le PATH
    echo Veuillez installer Python depuis https://python.org
    pause
    exit /b 1
)

echo.
echo Verification de FFmpeg...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo AVERTISSEMENT: FFmpeg n'est pas installe ou pas dans le PATH
    echo Le script pourra extraire les heures mais ne pourra pas modifier les metadonnees
    echo Installez FFmpeg depuis https://ffmpeg.org/download.html
    echo.
)

echo Installation des dependances Python...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ERREUR: Echec de l'installation des dependances
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Installation terminee avec succes !
echo ==========================================
echo.
echo Vous pouvez maintenant utiliser le script :
echo python timecode_extractor.py "votre_fichier.mp4"
echo.
echo Ou utilisez timecode_batch.bat pour le glisser-deposer
echo.
pause
