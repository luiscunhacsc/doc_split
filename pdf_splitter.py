import os
import re
from PyPDF2 import PdfReader, PdfWriter
from tkinter import Tk, filedialog

def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip()

def extract_sections_by_bookmarks(input_pdf, book_title):
    clean_title = sanitize_filename(book_title)
    output_dir = f"capitulos_{clean_title}"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    reader = PdfReader(input_pdf)
    outlines = reader.outline
    top_level_bookmarks = [outline for outline in outlines if not isinstance(outline, list)]
    
    for i, bookmark in enumerate(top_level_bookmarks):
        title = bookmark['/Title']
        page_num = reader.get_destination_page_number(bookmark)

        if i < len(top_level_bookmarks) - 1:
            end_page = reader.get_destination_page_number(top_level_bookmarks[i + 1]) - 1
        else:
            end_page = len(reader.pages) - 1
        
        writer = PdfWriter()
        for j in range(page_num, end_page + 1):
            writer.add_page(reader.pages[j])
        
        clean_chapter_title = sanitize_filename(title)
        output_file = os.path.join(output_dir, f"{i+1:02d}_{clean_chapter_title}.pdf")
        
        with open(output_file, 'wb') as out_file:
            writer.write(out_file)
        
        print(f"✅ Criado: {output_file} (Páginas {page_num+1} a {end_page+1})")

if __name__ == "__main__":
    print("📂 Seleciona o ficheiro PDF que queres segmentar...")

    root = Tk()
    root.withdraw()
    input_pdf = filedialog.askopenfilename(
        title="Seleciona o PDF do livro",
        filetypes=[("Ficheiros PDF", "*.pdf")]
    )
    
    if not input_pdf:
        print("❌ Nenhum ficheiro selecionado. A operação foi cancelada.")
    else:
        print(f"📝 Ficheiro selecionado: {input_pdf}")
        book_title = input("📘 Introduz o título do livro (será usado para nomear a pasta): ").strip()
        if not book_title:
            print("❌ Título inválido. A operação foi cancelada.")
        else:
            extract_sections_by_bookmarks(input_pdf, book_title)
            print("\n✅ Segmentação concluída com sucesso.")