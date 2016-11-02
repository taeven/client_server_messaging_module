import socket
client = socket.socket()
client.connect(('127.0.1.1', 1234))
while True:
    data = input()
    client.send(data.encode())
    if data == 'disconnect':
        break
