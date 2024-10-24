from scapy.all import *

ping = ICMP(type=8)

packet = IP(src="192.168.0.10", dst="192.168.1.99")  # IP source et destination

frame = Ether(src="28:7f:cf:99:86:8a", dst="00:1a:2b:3c:4d:5e")  # MAC source et destination

final_frame = frame / packet / ping

answers, unanswered_packets = srp(final_frame, timeout=10)

print(f"Pong reçu : {answers[0]}")




