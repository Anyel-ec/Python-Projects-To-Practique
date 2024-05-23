from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

# Filtra paquetes IPv4
sniff(prn=packet_callback, filter="ip", store=0)
