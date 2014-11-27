from tkinter import *
from mt_client import *
from functools import partial

class ChatGui:



    def __init__(self, sender_object):
        sender = sender_object
        self.activate_gui(sender)

    def activate_gui(self, sender):
        self.main = Tk()
        self.main.title('ChatUp')
        self.txtChat=Text(self.main, height=20, width=50, bg="#bbbbbb")
        self.txtChat.pack(side=TOP)
        self.strInput = str()
        self.txtInput = Entry(self.main,  width=40, textvariable=self.strInput)
        self.txtInput.pack(side = LEFT)
        submit_function = partial(self.submit, sender)
        self.cmdSubmit = Button(self.main, width=10, command=submit_function, text="Submit")
        self.cmdSubmit.pack(side=RIGHT)
        self.main.mainloop()



    #on button click
    def submit(self, sender):
        print("submit")
        message = self.txtInput.get()
        sender.send_data(sender.sock, message)

    def writeLine(self, strMessage):
        self.txtChat.insert(END, strMessage + "\n")


#main.mainloop()
