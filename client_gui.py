from tkinter import *
import socket
import threading

client = socket.socket()

root = Tk()
root.title('client version')
root.geometry('500x600')
bott = Frame(root, bg='yellow')
client.connect(('172.16.141.167', 5000))


def recieve_data():
    while True:
        try:

            data = client.recv(1024)
            data = data.decode()
            show_mess.configure(state='normal')
            show_mess.insert(END, data + '\n')
            show_mess.configure(state='disable')
            message_type.delete(0, END)

        except Exception:
            print('ended')
            show_mess.insert(END, 'connection closed')


def send_data(event):
    data = message_type.get()
    data = data.encode()
    client.send(data)
    message_type.delete(0, END)


bott.pack(side=BOTTOM, fill=X)
send_butt = Button(bott, text='send', bg='green', fg='white')
send_butt.bind('<Button-1>', send_data)
send_butt.pack(side=LEFT)

message_type = Entry(bott, bg='white')
message_type.bind('<Return>', send_data)
message_type.pack(side=LEFT)

show_mess = Text(root)
show_mess.configure(state='disable')
show_mess.pack(side=LEFT, fill=BOTH)

t = threading.Thread(target=recieve_data)
t.daemon = True
t.start()
#recieve_data()


root.mainloop()


