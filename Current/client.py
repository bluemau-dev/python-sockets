#!/usr/bin/env python3

# 2 - Client Initiates a connection

import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

# 3 - Data is exchanged

    # b: Data sent in 8-bit units.
    s.sendall(b"Hello World.")
    data = s.recv(1024)

print(f"Received {data}")