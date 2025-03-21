#!/bin/bash

# ▶️ Run PDF Splitter - Linux/macOS
# Activates the virtual environment and runs the script

if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please run setup.sh first."
    exit 1
fi

source .venv/bin/activate
python pdf_splitter.py