import requests
from bs4 import BeautifulSoup

# URL de la página web a analizar
url = 'https://example.com'

# Realizar la solicitud GET para obtener el contenido de la página
response = requests.get(url)

# Verificar que la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsear el contenido HTML utilizando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos los elementos <h1> y <p>
    h1_elements = soup.find_all('h1')
    p_elements = soup.find_all('p')
    
    # Filtrar los elementos relacionados con temas de seguridad
    security_related_h1 = [h1.text.strip() for h1 in h1_elements if 'seguridad' in h1.text.lower()]
    security_related_p = [p.text.strip() for p in p_elements if 'seguridad' in p.text.lower()]
    
    # Imprimir los resultados
    print("Elementos <h1> relacionados con seguridad:")
    for title in security_related_h1:
        print("- ", title)
    
    print("\nElementos <p> relacionados con seguridad:")
    for paragraph in security_related_p:
        print("- ", paragraph)
else:
    print("Error al realizar la solicitud GET:", response.status_code)
