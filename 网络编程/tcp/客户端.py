import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.50.27', 8000))
data = '发送的内容'
s.sendto(data.encode(), ('192.168.50.27', 8000))
s.close()
