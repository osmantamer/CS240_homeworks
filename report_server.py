import socket, json

class Server:
    def __init__(self, host="", port=1234):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
        print('starting up on {} port {}'.format(*self.server_address))

    def startListen(self):
        self.sock.bind(self.server_address)
        self.sock.listen(1)
        self.receiveData()

    def receiveData(self):
        while True:
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                print('connection from', client_address)
                while True:
                    data = connection.recv(1024)
                    print('received {}'.format(data.decode('unicode-escape')))
                    if data:
                        data_loaded = json.loads(data.decode('unicode-escape'))  # data loaded
                        print(type(data_loaded), data_loaded)
                        print('sending data back to the client')
                        connection.sendall(data)
                    else:
                        print('no data from', client_address)
                        break

            finally:
                connection.close()

ser = Server()
ser.startListen()