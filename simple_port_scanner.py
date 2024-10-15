import socket

target_ip = '127.0.0.1'
open_ports = []

def scan_port(port_number):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.1)
    result = sock.connect_ex((target_ip, port_number))
    if result == 0:
        open_ports.append(port_number)
    sock.close()

for port in range(1, 10000):
    scan_port(port)

print("Open ports:", open_ports)
