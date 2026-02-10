@echo off
echo ====================================================
echo Setting up PII Detector Local Environment
echo ====================================================

:: 1. Create Virtual Environment
if not exist venv (
    echo [1/3] Creating virtual environment...
    python -m venv venv
) else (
    echo [1/3] Virtual environment already exists.
)

:: 2. Activate and Install Requirements
echo [2/3] Installing dependencies (this may take a minute)...
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

:: 3. Verify Folders
echo [3/3] Checking project structure...
if not exist models (
    echo WARNING: 'models' folder not found! Please place your BERT weights in a 'models' directory.
)
if not exist src (
    echo ERROR: 'src' folder missing. Ensure your scripts are in the 'src' directory.
)

echo ====================================================
echo SETUP COMPLETE!
echo To start detecting PII, run: 
echo venv\Scripts\activate
echo python -m src.inference
echo ====================================================
pause