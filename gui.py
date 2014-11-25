from tkinter import *

class ChatGui:

    def __init__(self):
        self.main = Tk()
        self.main.title('ChatUp')
        self.strInput = str()
        self.txtChat=Text(self.main, height=20, width=50, bg="#bbbbbb")
        self.txtChat.pack(side=TOP)
        self.txtInput = Entry(self.main,  width=40, textvariable=self.strInput)
        self.txtInput.pack( side = LEFT)
        self.cmdSubmit = Button(self.main, width=10, command=self.submit, text="Submit")
        self.cmdSubmit.pack(side=RIGHT)
        self.main.mainloop()

    def submit(self):
        self.txtChat.insert(END,"submit\n")

#main.mainloop()
