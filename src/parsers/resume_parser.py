import pdfplumber

def extract_resume_text(pdf_path: str) -> str:
    """
    Extract text from a resume PDF.

    Args:
        pdf_path (str): Path to the pdf file.

    Returns:
        str: Extracted text from all pages.
    """

    extracted_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + "\n"

        return extracted_text

    except Exception as e:
        raise Exception(f"Error while reading resume PDF: {e}")

