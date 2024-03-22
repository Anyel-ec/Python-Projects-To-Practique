import nmap

def discover_hosts(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')

    hosts_list = []
    for host in nm.all_hosts():
        hosts_list.append(host)
    return hosts_list

def main():
    ip_range = input("Ingrese el rango de IP a escanear (Ejemplo: 192.168.1.0/24): ")
    hosts = discover_hosts(ip_range)

    print("Hosts descubiertos:")
    for host in hosts:
        print(host)

if __name__ == "__main__":
    main()
