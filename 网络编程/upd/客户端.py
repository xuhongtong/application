import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = '呵呵'
s.sendto(data.encode(), ('192.168.50.27', 8000))
