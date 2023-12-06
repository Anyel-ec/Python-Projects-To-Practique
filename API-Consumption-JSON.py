import requests

def consumir_servicio(url):
    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Analizar el JSON de la respuesta
            data = response.json()

            # Procesar los datos según tus necesidades
            for key, value in data.items():
                print(f"{key}: {value}")

        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")

    except Exception as e:
        print(f"Error en la solicitud: {e}")

# URL del servicio que devuelve un archivo JSON (reemplázala con la URL correcta)
url_servicio = "https://ejemplo.com/servicio_json"

# Llamar a la función de consumo del servicio
consumir_servicio(url_servicio)
