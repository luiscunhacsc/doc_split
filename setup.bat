@echo off
REM 📦 PDF Splitter - Windows Setup Script
REM This script sets up a virtual environment and installs the required dependencies

echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
CALL .venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo ✅ Setup complete. Run the tool with: python pdf_splitter.py