import pdfplumber
import PyPDF2
import os

def extract_text(filepath):
    """
    Extracts text from a .pdf or .txt file.
    Uses pdfplumber as primary and PyPDF2 as fallback for PDFs.
    """
    text = ""
    ext = os.path.splitext(filepath)[1].lower()

    if ext == '.pdf':
        try:
            # Primary: pdfplumber
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print(f"pdfplumber failed: {e}. Falling back to PyPDF2.")
            try:
                # Fallback: PyPDF2
                with open(filepath, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
            except Exception as e2:
                print(f"PyPDF2 also failed: {e2}")
    
    elif ext == '.txt':
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='latin-1') as f:
                text = f.read()

    return text.strip()
