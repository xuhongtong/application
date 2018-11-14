import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8000))
data='hello'
client.send(data.encode())
client.close()