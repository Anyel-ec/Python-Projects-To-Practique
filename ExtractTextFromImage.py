from PIL import Image
import pytesseract

# Abre la imagen utilizando PIL (Python Imaging Library)
imagen = Image.open('imagen.png')

# Utiliza pytesseract para extraer el texto de la imagen
texto_extraido = pytesseract.image_to_string(imagen)

# Imprime el texto extraído
print(texto_extraido)
