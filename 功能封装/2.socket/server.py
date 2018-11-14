import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen(5)
client, address = server.accept()
msg = client.recv(1024)
print(msg.decode())
server.close()


class SocketServer:
    def __init__(self):
        self.server = self.get_server
        self.bind = self.get_bind
        self.listen = self.get_listen
        self.accept=self.get_accept
        self.msg=self.get_rev

    @property
    def get_server(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def get_bind(self, b=('127.0.0.1', 8000)):
        return self.server.bind(b)

    @property
    def get_listen(self, num=5):
        return self.server.listen(num)

    @property
    def get_accept(self):
        return self.server.accept()

    @property
    def get_rev(self,size=1024):
        client,address=self.accept
        return client.recv(size)

    def show(self):
        print(self.msg.decode())


if __name__=='__main__':
    s=SocketServer()
    s.get_accept()