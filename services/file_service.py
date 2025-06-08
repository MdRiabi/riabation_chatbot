import os
from PyPDF2 import PdfReader

SUPPORTED_EXTENSIONS = [".pdf", ".txt", ".chat"]

def extract_text(uploaded_file) -> str:
    """
    Extrait le texte brut d'un fichier PDF, TXT ou CHAT téléchargé.
    """

    file_ext = os.path.splitext(uploaded_file.name)[1].lower()

    if file_ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Extension de fichier non supportée : {file_ext}")

    try:
        if file_ext == ".pdf":
            return _extract_text_from_pdf(uploaded_file)
        elif file_ext in [".txt", ".chat"]:
            return _extract_text_from_text_file(uploaded_file)
    except Exception as e:
        return f"❌ Erreur lors de l'extraction : {str(e)}"

def _extract_text_from_pdf(file) -> str:
    """Extraction de texte depuis un fichier PDF (texte uniquement, pas OCR)."""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

def _extract_text_from_text_file(file) -> str:
    """Lecture brute du fichier texte (TXT/CHAT), décodé en UTF-8."""
    return file.read().decode("utf-8", errors="ignore").strip()
