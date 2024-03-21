import requests

def scan_website(url):
    api_key = 'tu_api_key_aqui'  # Reemplaza 'tu_api_key_aqui' con tu API key de SecurityTrails
    endpoint = f'https://api.securitytrails.com/v1/website/{url}/security'
    
    headers = {
        'APIKEY': api_key
    }

    try:
        response = requests.get(endpoint, headers=headers)
        data = response.json()

        if 'status' in data and data['status'] == 'error':
            print(f"Error: {data['message']}")
        else:
            vulnerabilities = data['data']['vulnerabilities']
            print("Vulnerabilidades encontradas:")
            for vuln in vulnerabilities:
                print(f"- {vuln['title']}: {vuln['description']}")
                print(f"  Solución: {vuln['solution']}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    url = input("Ingrese la URL del sitio web que desea escanear: ")
    scan_website(url)
