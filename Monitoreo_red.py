from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Captura paquetes en la interfaz especificada
sniff(iface="Wi-Fi", prn=packet_callback, store=0) # Este es de mi adaptador Wifi
