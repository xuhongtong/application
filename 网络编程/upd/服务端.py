import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.50.27', 8000))
receive_data, client_address = s.recvfrom(1024)
print(receive_data.decode(), client_address)
s.close()
