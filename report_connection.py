import socket, json, threading

class MySocket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))
        print("connected!")

    def send_data(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:].encode('utf-8'))
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        ans = self.sock.recv(1024).decode('unicode-escape')
        print(ans)

conn = MySocket()
conn.connect("89.19.20.130", 12345)
my_data = {"report_id": "12345","key_words":["hello","wşorld","my","name","is","osman"]}
data_string = json.dumps(my_data) #data serialized
conn.send_data(data_string)