import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.settimeout(1)
    server_address = ('127.0.0.1', 3000)
    result = client_socket.connect_ex(server_address)

    if result == 0:
        print("Port open")
        client_socket.sendall(b'GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n')
        full_response = b""

        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            full_response += data

        print("Full Response from server:")
        print(full_response.decode('utf-8'))
    else:
        print("Port closed or unreachable")

finally:
    client_socket.close()
