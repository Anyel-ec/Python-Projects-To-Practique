from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import json

def json_to_pdf(json_data, pdf_path):
    # Abre el archivo JSON y carga los datos
    with open(json_data, 'r') as file:
        data = json.load(file)

    # Crea el documento PDF
    pdf = SimpleDocTemplate(pdf_path, pagesize=letter)

    # Convierte los datos JSON a una lista de listas para la tabla
    table_data = [list(data[0].keys())]  # Encabezados de la tabla
    for item in data:
        table_data.append(list(item.values()))

    # Crea la tabla y establece el estilo
    table = Table(table_data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Agrega la tabla al documento PDF
    pdf.build([table])

# Ejemplo de uso
json_file_path = 'ejemplo.json'  # Reemplaza con la ruta de tu archivo JSON
pdf_output_path = 'output.pdf'  # Ruta de salida para el PDF

json_to_pdf(json_file_path, pdf_output_path)
