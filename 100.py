import socket

target_ip = '127.0.0.1'
open_ports = []

def scan_port(port_number):
    # Create a new TCP (SOCK_STREAM) socket using the IPv4 address family (AF_INET)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout of 0.1 seconds for the connection attempt to prevent long delays on unresponsive ports.
    sock.settimeout(0.1)

    # Attempt to connect to the target IP on the specified port using the connect_ex() method.
    # This method returns 0 if the connection is successful (i.e., the port is open), otherwise, it returns an error code.
    result = sock.connect_ex((target_ip, port_number))

    # If the connection was successful (result == 0), add the port number to the open_ports list.
    if result == 0:
        open_ports.append(port_number)
    sock.close()

for port in range(1, 6000):
    scan_port(port)

print("Open ports:", open_ports)
