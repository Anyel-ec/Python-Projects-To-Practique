from reportlab.pdfgen import canvas

def generate_pdf(text, file_name='output.pdf'):
    # Create a PDF canvas
    pdf = canvas.Canvas(file_name)

    # Set page size
    page_width, page_height = 400, 600  # You can adjust these values as needed
    pdf.setPageSize((page_width, page_height))

    # Coordinates to start writing text
    x, y = 50, page_height - 100

    # Maximum characters per line
    max_characters_per_line = 50

    # Split the text into lines
    lines = [text[i:i + max_characters_per_line] for i in range(0, len(text), max_characters_per_line)]

    # Write each line to the PDF canvas
    for line in lines:
        pdf.drawString(x, y, line)
        y -= 20  # Adjust the line spacing as needed

    # Save the PDF
    pdf.save()

    print(f"PDF file created: {file_name}")

if __name__ == "__main__":
    # You can change the text as per your preference
    text_for_pdf = """
    This is an example text for the PDF.
    You can provide your own text when running the script.
    """

    # Generate the PDF with the provided text
    generate_pdf(text_for_pdf)
