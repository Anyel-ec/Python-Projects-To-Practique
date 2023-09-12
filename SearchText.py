import requests
from bs4 import BeautifulSoup

# URL de la página que deseas analizar
url = 'https://www.ejemplo.com'

# Lista de palabras clave que deseas buscar
palabras_clave = ["IA", "machine learning", "inteligencia artificial", "algoritmo"]

# Realiza una solicitud HTTP para obtener el contenido de la página
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Parsea el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encuentra y extrae todo el texto de la página
    texto_pagina = soup.get_text()
    
    # Inicializa un contador para cada palabra clave
    contador_palabras = {palabra: 0 for palabra in palabras_clave}
    
    # Convierte el texto de la página en minúsculas para una búsqueda insensible a mayúsculas
    texto_pagina = texto_pagina.lower()
    
    # Itera a través de las palabras clave y cuenta sus ocurrencias
    for palabra in palabras_clave:
        contador_palabras[palabra] = texto_pagina.count(palabra.lower())
    
    # Imprime los resultados
    for palabra, contador in contador_palabras.items():
        print(f'La palabra "{palabra}" aparece {contador} veces en la página.')
else:
    # Si la solicitud no fue exitosa, muestra un mensaje de error
    print(f'Error al obtener la página. Código de respuesta: {response.status_code}')
