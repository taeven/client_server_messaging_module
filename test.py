from tkinter import *
from tkinter.ttk import *


class firstexample:
    def __init__(self, master):
        app = Frame(master)
        app.grid()


        butt1 = Button(app, text='1st one')
        butt1.bind("<Button-1>", self.left_cl)
        butt1.bind("<Button-2>", self.middle_cl);
        butt1.bind("<Button-3>", self.right_cl)

        butt1.grid(row=0, column=0)
        l1 = Label(app, text="shitty window")
        l1.grid()

        butt2 = Button(app, command=app.quit)
        butt2.configure(text="2nd one")
        butt2.grid(row=0, column=1)

    def left_cl(self, event):
        print("left click")

    def right_cl(self, event):
        print("right click")

    def middle_cl(self, event):
        print("middle clicked")


def do_print():
    print("clicked menu")

root = Tk()
root.title('example')
root.geometry('200x200')

main_menu = Menu(root)
root.config(menu=main_menu)

sub_menu = Menu(main_menu)
main_menu.add_cascade(label="file", menu=sub_menu);
sub_menu.add_command(label="first one", command=do_print)
main_menu.bind();


obj = firstexample(root)
root.mainloop()






