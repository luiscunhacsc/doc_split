@echo off
echo Building executable with PyInstaller...
python -m pyinstaller pdf_splitter.spec
echo ✅ Done! Check the "dist" folder for your .exe file.
pause
