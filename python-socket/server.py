"""Socket are endpoints that receive data."""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
""" AF_INET corresponds to IPV4
	SOCK_STREAM corresponds for TCP """

s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")
	clientsocket.send(bytes("Welcome!!!", "utf-8"))
	clientsocket.close()