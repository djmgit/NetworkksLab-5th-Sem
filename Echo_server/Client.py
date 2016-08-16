import socket
sock=socket.socket()
host=socket.gethostname()
port=12345
#connecting to server
sock.connect((host,port))

mesg=raw_input("Enter message : ")
#sending message
sock.send(mesg)
#receiving message from server
mesg_server=sock.recv(1024)
print 'Received from server : '+mesg_server
print 'client terminated'	
