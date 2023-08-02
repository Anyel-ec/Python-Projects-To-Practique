import socket

def scan_ports(target_host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        print(f"Escaneando puerto {port}...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout para la conexión, en segundos
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


target_host = input("Ingresa la dirección IP o el nombre de dominio del computador a escanear: ")
start_port = int(input("Ingresa el número del primer puerto del rango a escanear: "))
end_port = int(input("Ingresa el número del último puerto del rango a escanear: "))

open_ports = scan_ports(target_host, start_port, end_port)

if open_ports:
    print(f"Los siguientes puertos están abiertos en {target_host}:")
    print(open_ports)
else:
    print(f"No se encontraron puertos abiertos en {target_host}.")
