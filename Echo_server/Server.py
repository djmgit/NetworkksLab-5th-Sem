import socket
sock=socket.socket()
# getting host name
host=socket.gethostname()
port=12345
# binding port to server
sock.bind((host,port))
sock.listen(5)	
print 'Server started, listening at host: '+str(host)+' port: '+str(port)
while True:
	# accepting connection
	con,addr=sock.accept()
	print 'got connection from '+str(addr)
	# receiving message
	mesg=con.recv(1024)
	# sending message
	con.send(mesg)
	# closing connection
	con.close()
	

print 'Server terminated'