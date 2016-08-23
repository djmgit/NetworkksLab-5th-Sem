import socket
s=socket.socket()
server_host=''
server_port=12348
s.connect((server_host,server_port))


nums=raw_input("Enter numbers separated by space : ")
s.send(nums)
res=s.recv(1024)
print res