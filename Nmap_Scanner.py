import nmap

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
                print('Puerto : %s\tEstado : %s' % (port, scanner[host][proto][port]['state']))
                print('Servicio : %s' % scanner[host][proto][port]['name'])
                print('')

if __name__ == '__main__':
    ip_a_escanear = '192.168.1.1'  
    escanear_vulnerabilidades(ip_a_escanear)
