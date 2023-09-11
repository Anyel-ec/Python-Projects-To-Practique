import requests
from bs4 import BeautifulSoup

# URL de la página que deseas analizar
url = 'https://www.ejemplo.com'

# Realiza una solicitud HTTP para obtener el contenido de la página
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Parsea el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encuentra y extrae todo el texto de la página
    texto_pagina = soup.get_text()
    
    # Imprime el texto
    print(texto_pagina)
else:
    # Si la solicitud no fue exitosa, muestra un mensaje de error
    print(f'Error al obtener la página. Código de respuesta: {response.status_code}')
