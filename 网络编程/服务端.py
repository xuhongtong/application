import socket

s = socket.socket(socket.AF_INET)
s.bind(('192.168.50.27', 8000))
s.listen(5)
client, address = s.accept()
data = client.recv(1024)
print(data.decode())
s.close()
