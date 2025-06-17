from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from summarizer2 import summarize_text

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_file (BytesIO): The uploaded PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    reader = PdfReader(pdf_file)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

def save_summary_to_pdf(summary, output_file):
    """
    Saves the summarized text into a new PDF file.

    Args:
        summary (str): The summarized text.
        output_file (BytesIO): File-like object to save the PDF content.
    """
    c = canvas.Canvas(output_file)
    c.drawString(100, 800, "Summary:")
    lines = summary.split("\n")
    y_position = 780
    for line in lines:
        c.drawString(100, y_position, line)
        y_position -= 20  # Adjust spacing between lines
        if y_position < 50:  # New page if out of space
            c.showPage()
            y_position = 800
    c.save()
