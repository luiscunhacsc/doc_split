#!/bin/bash

# 📦 PDF Splitter - Linux/macOS Setup Script
# This script sets up a virtual environment and installs the required dependencies

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete. Run the tool with: python pdf_splitter.py"