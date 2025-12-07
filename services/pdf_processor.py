import PyPDF2
from io import BytesIO

def extract_text_from_pdf(file: BytesIO) -> str:
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for num_page, page in enumerate(reader.pages, 1):
            text_page = page.extract_text()
            if text_page.strip():
                text += f"\n\n--- Page {num_page} ---\n\n"
                text += text_page + "\n"

        text = text.strip()
        if not text:
            return "Error: El PDF parece estar vacío o no contiene texto extraíble."
        return text
    except Exception as e:
      return f"Error al extraer texto del PDF: {e}"