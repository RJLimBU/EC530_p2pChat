import socket

# INET means IPv4, DGRAM means UDP
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
targetAddr = "168.122.0.230"
hostaddr = bytes(socket.gethostname(), 'utf-8')
helloMsg = bytes("connection from {}".format(hostaddr), 'utf-8')
soc.sendto(helloMsg, (targetAddr,9000))

while True:
	msg = input('Type your message: ')
	msg = bytes(msg, 'utf-8')
	soc.sendto(msg, (targetAddr,9000))

	print('client socket: {}'.format(soc.getsockname()))
	print('status: {}'.format(soc.recv(1024)))
	print('previous sent message: {}'.format(soc.recv(1024)))
	print()

soc.close()
