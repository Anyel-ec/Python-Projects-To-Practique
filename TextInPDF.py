from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Nombre del archivo de salida PDF
nombre_archivo = "mi_documento.pdf"

# Texto que deseas incluir en el PDF
texto = """
Este es un ejemplo de cómo exportar texto a un archivo PDF utilizando la librería reportlab en Python.
Puedes personalizar este texto según tus necesidades.
"""

# Crear un archivo PDF y configurar el tamaño de la página
c = canvas.Canvas(nombre_archivo, pagesize=letter)

# Definir la fuente y el tamaño del texto
c.setFont("Helvetica", 12)

# Insertar el texto en el PDF
c.drawString(100, 700, texto)

# Guardar el PDF
c.save()

print(f"El archivo PDF '{nombre_archivo}' ha sido creado con éxito.")
