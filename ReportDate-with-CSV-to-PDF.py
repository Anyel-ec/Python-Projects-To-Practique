import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def leer_csv(nombre_archivo):
    # Leer el archivo CSV y devolver un DataFrame de pandas
    return pd.read_csv(nombre_archivo)

def generar_pdf(datos):
    # Configurar el tamaño del PDF
    c = canvas.Canvas("datos.pdf", pagesize=letter)
    
    # Configurar el tamaño de la fuente y el espacio entre líneas
    c.setFont("Helvetica", 12)
    espacio_linea = 15
    
    # Iterar sobre los datos y escribirlos en el PDF
    for fila, (_, datos_fila) in enumerate(datos.iterrows()):
        # Escribir cada campo de la fila en una nueva línea
        for columna, valor in datos_fila.iteritems():
            texto = f"{columna}: {valor}"
            c.drawString(100, 800 - (espacio_linea * (fila + 1)), texto)
    
    # Guardar el PDF generado
    c.save()

if __name__ == "__main__":
    nombre_archivo = "datos.csv"
    
    # Leer datos del archivo CSV
    datos = leer_csv(nombre_archivo)
    
    # Generar PDF con los datos
    generar_pdf(datos)
