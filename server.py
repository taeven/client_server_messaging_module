import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '172.16.141.167'
port = 5000
address = (ip, port)
server.bind(address)
lock = threading.Lock()


server.listen(2)
print('listening on ip '+ip)


def broadcast(data):
    lock.acquire()
    for i in client:
        i.send(data)
    lock.release()


def receive_data(clt, addrs):

    while True:

        data = clt.recv(1024)
        broadcast(data)
        data = data.decode()
        print(addrs, " ", data)
        if not data:
            break
        if data == 'disconnect':
            break

client = []
i = 0
while True:
    tmp, addr = server.accept()
    client.append(tmp)
    print('listening from ip ', addr)
    t = threading._start_new_thread(receive_data, (tmp, addr, ))


server.close()
