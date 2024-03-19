import nmap
from vulners import Vulners

def obtener_info_servicio(service_name):
    vulners = Vulners()

    # Buscar información sobre la vulnerabilidad utilizando Vulners API
    results = vulners.softwareVulnerabilities(service_name)
    
    if not results:
        return "No se encontraron vulnerabilidades conocidas."
    
    # Imprimir las vulnerabilidades encontradas y sus recomendaciones
    for result in results:
        print(f"Vulnerabilidad: {result['title']}")
        print(f"Descripción: {result['description']}")
        print(f"Recomendación: {result['recommendation']}")
        print("")

def escanear_vulnerabilidades(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments='-p 1-65535 -T4 -A -v')

    for host in scanner.all_hosts():
        print('Host : %s (%s)' % (host, scanner[host].hostname()))
        print('State : %s' % scanner[host].state())

        for proto in scanner[host].all_protocols():
            print('Protocolo : %s' % proto)

            lport = scanner[host][proto].keys()
            for port in lport:
                port_info = scanner[host][proto][port]
                print('Puerto : %s\tEstado : %s' % (port, port_info['state']))
                print('Servicio : %s' % port_info['name'])
                
                # Verificar si hay información de vulnerabilidad disponible
                if 'product' in port_info and 'version' in port_info:
                    servicio = f"{port_info['product']} {port_info['version']}"
                    print('Servicio detectado: ', servicio)
                    obtener_info_servicio(servicio)
                print('')


if __name__ == '__main__':
    ip_a_escanear = '127.0.0.1'  # Cambia esta IP por la dirección de tu red que deseas escanear
    escanear_vulnerabilidades(ip_a_escanear)
