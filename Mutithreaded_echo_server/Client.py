import socket
s=socket.socket()

s.connect(('',12346))
while True:
	mesg=raw_input("Enter message : ")

	s.send(mesg)
	if mesg=='exit':
		exit(0)
	print 'received from server : ',s.recv(1024)
