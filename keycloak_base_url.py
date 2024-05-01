import requests

# Configuración
keycloak_base_url = 'http://localhost:8080/auth/realms/your_realm'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
username = 'your_username'
password = 'your_password'

# Obtener el token de acceso utilizando el flujo de contraseña
token_url = f'{keycloak_base_url}/protocol/openid-connect/token'
payload = {
    'grant_type': 'password',
    'client_id': client_id,
    'client_secret': client_secret,
    'username': username,
    'password': password
}

response = requests.post(token_url, data=payload)
token_data = response.json()
access_token = token_data['access_token']

# Hacer una solicitud utilizando el token de acceso
api_url = 'http://your_api_endpoint'
headers = {'Authorization': f'Bearer {access_token}'}

response = requests.get(api_url, headers=headers)

# Procesar la respuesta
if response.status_code == 200:
    print('Respuesta exitosa:')
    print(response.json())
else:
    print('Error al hacer la solicitud:')
    print(response.text)
