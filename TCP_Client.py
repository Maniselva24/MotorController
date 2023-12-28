# tcp client

import socket


def tcp_com(x):
    host = "192.168.1.9"  # "192.168.1.9 (STATION MODE)" 192.168.4.1(SOFT ACCESS POINT MODE) # The server's hostname or IP address
    port = 1336  # The port used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect((host, port))
            s.sendall(bytes(x, encoding='utf-8'))
            # data = s.recv(8)    # will receive 8 bytes
            s.close()
        except socket.error as exc:
            print("Caught exception socket.error : %s" % exc)
# print(f"Received {data!r}")
