import threading
import socket

class Serve(threading.Thread):
	def __init__(self,client):
		threading.Thread.__init__(self)
		self.client=client
	def run (self) :
		exit=False
		while not exit:
			mesg=self.client[0].recv(1024)
			print 'received ',mesg,' from ',self.client[1]
			if mesg=='exit':
				print 'connection from ',self.client[1],' lost'
				self.client[0].close()
				exit=True
			else:	
				self.client[0].send(mesg)	


workers=[]
s=socket.socket()
s.bind(('',12346))
s.listen(5)
while True:
	con,addr=s.accept()
	print 'connetion received from ',addr
	t=Serve((con,addr))
	t.start()
	workers.append(t)


