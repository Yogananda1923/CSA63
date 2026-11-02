from scapy.all import *

print("Starting Packet Sniffing...")

def capture(packet):
    print("Captured Packet:", packet.summary())

sniff(prn=capture, count=5)
