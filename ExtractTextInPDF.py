import PyPDF2

def extraer_texto_pdf(archivo_pdf):
    texto = ""
    
    # Abre el archivo PDF en modo de lectura binaria
    with open(archivo_pdf, "rb") as pdf_file:
        # Crea un objeto PDFReader
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        # Itera a través de cada página del PDF
        for pagina in range(pdf_reader.numPages):
            # Extrae el texto de la página actual
            pagina_actual = pdf_reader.getPage(pagina)
            texto += pagina_actual.extractText()
    
    return texto

# Nombre del archivo PDF que deseas procesar
archivo_pdf = "ejemplo.pdf"

# Llama a la función para extraer el texto
texto_extraido = extraer_texto_pdf(archivo_pdf)

# Imprime el texto extraído
print(texto_extraido)
