import socket

defaultPort = 9000
clientaddr = '168.122.0.230'
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((clientaddr, 9000))

while True:
	clientList = []

	while True:

		data, client_address =  soc.recvfrom(2048)
		print('client address: ',client_address)
		print('message: ',data)
		print()
		#msg = data
		soc.sendto(b'ready', client_address)
		soc.sendto(data, client_address)

		if len(clientList) >= 2:
			print('got 2 clients, sending details to each')
			break

	c1 = clients.pop()
	c1_addr, c1_port = c1
	c2 = clients.pop()
	c2_addr, c2_port = c2

	sock.sendto('{} {} {}'.format(c1_addr, c1_port, defaultPort).encode(), c2)
	sock.sendto('{} {} {}'.format(c2_addr, c2_port, defaultPort).encode(), c1)


