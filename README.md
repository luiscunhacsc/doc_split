# 📚 PDF Splitter by Bookmarks (Chapters)

This tool automatically splits a PDF file into separate PDFs based on **top-level bookmarks** (chapters or sections) defined inside the PDF. It’s especially useful for:

- Organizing books, manuals, or lecture notes into chapters;
- Summarizing chapters using tools like ChatGPT;
- Translating structured documents section by section;
- Studying or sharing only relevant parts of a large document.

---

## 🚀 Quick Start (The Easy Way)

If you don’t want to deal with Python commands, we’ve got you covered:

### 🖥️ Windows

1. Double-click `setup.bat` to install everything (just once).
2. Then double-click `run.bat` to start the program!

### 🍏 Linux / macOS

1. Open a terminal in the project folder.
2. Run the following:
   ```bash
   bash setup.sh
   bash run.sh
   ```

✅ These scripts will:
- Set up a virtual environment for you
- Install all the necessary packages
- Launch the tool with a graphical file picker

---

## ⚠️ Legal and Ethical Notice

> This program assumes you have the **legal right** to manipulate the PDF file.  
> Use it only with materials you **own**, that are in the **public domain**, or under an **appropriate license**.
>
> The author of this tool **respects copyright laws** and buys all books and materials that are valuable for professional or personal growth.  
> We believe in using technology for good — **use at your own risk**.

---

## ⚙️ Manual Setup (for developers and advanced users)

### 📌 1. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 📦 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 🧪 3. Run the Script

```bash
python pdf_splitter.py
```

A file dialog will open for you to select the PDF. Then the terminal will ask for the book title. The chapters will be saved in a folder like:

```
chapters_Book-Title/
```

---

### 🛠️ Build a Standalone Executable (.exe)

If you're on Windows and want a single-click executable:

```bash
pip install pyinstaller
pyinstaller pdf_splitter.spec
```

Output will be in the `dist/` folder.

---

## 📁 Project Contents

- `pdf_splitter.py` – Main script
- `pdf_splitter.spec` – PyInstaller config file
- `pdf_splitter_icon.ico` – Custom app icon
- `requirements.txt` – Project dependencies
- `setup.bat` / `setup.sh` – One-time setup scripts
- `run.bat` / `run.sh` – Run the tool easily

---

## 💡 Use Cases

- Summarizing chapters using ChatGPT
- Organizing study materials
- Translating structured documents
- Extracting and sharing specific parts of large PDFs

---

## ✅ Requirements

- Python 3.10 or higher
- OS: Windows, macOS, or Linux

---

📚 Organize your PDFs easily, ethically, and efficiently.