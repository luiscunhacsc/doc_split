@echo off
REM ▶️ Run PDF Splitter - Windows
REM Activates the virtual environment and runs the script

IF NOT EXIST ".venv\Scripts\activate.bat" (
    echo ❌ Virtual environment not found. Please run setup.bat first.
    EXIT /B 1
)

CALL .venv\Scripts\activate
python pdf_splitter.py