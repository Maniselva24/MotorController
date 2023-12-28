# tcp client

import socket

host = "192.168.1.9"  # "192.168.1.9 (STATION MODE)" 192.168.4.1(SOFT ACCESS POINT MODE) # The server's hostname or IP address
port = 1336  # The port used by the server


def tcp_send(x):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect((host, port))
            s.sendall(bytes(x, encoding='utf-8'))
            s.close()
        except socket.error as exc:
            return "Caught exception socket.error : %s" % exc
# print(f"Received {data!r}")
def tcp_receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(20)
        try:
            s.connect((host, port))
            data = s.recv(8)  # will receive 8 bytes
            return data
        except socket.error as exc:
            return exc
