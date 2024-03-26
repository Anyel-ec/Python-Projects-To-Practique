from flask import Flask, request, redirect, url_for, jsonify
from oauthlib.oauth2 import WebApplicationClient
import requests

app = Flask(__name__)

# Configura las credenciales de OAuth2 de Google
GOOGLE_CLIENT_ID = 'tu-client-id-de-google'
GOOGLE_CLIENT_SECRET = 'tu-client-secret-de-google'
GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'

client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Función de ayuda para obtener la URL de autorización de Google
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

# Ruta para iniciar sesión
@app.route('/login')
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Construye la URL de autorización de Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"]
    )
    return redirect(request_uri)

# Ruta de callback después de la autorización
@app.route('/login/callback')
def callback():
    code = request.args.get("code")

    # Intercambio de código de autorización por tokens de acceso
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Verifica la validez del token de acceso
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # Extrae los datos del usuario
    userinfo_data = userinfo_response.json()
    return jsonify(userinfo_data)

if __name__ == '__main__':
    app.run(debug=True)
