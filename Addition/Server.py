import socket
s=socket.socket()
host=''
port=12348
s.bind((host,port))
s.listen(5)

while True :
	con,addr=s.accept()
	nums=con.recv(1024)
	num1,num2=nums.split()
	num1,num2=int(num1),int(num2)
	r=num1+num2
	con.send(str(r))
	con.close()