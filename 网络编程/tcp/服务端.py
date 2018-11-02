import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.50.27', 8000))
# s.listen(5)
# client, address = s.accept()
# data = s.recv(1024)
receive_data,client_address=s.recv(1024)

print(receive_data.decode(),client_address)
s.close()
