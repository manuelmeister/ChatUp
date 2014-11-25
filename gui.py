from tkinter import *

def submit():
    print("subit")

main = Tk()
strInput = str()
lblChat = Text(main, height=20, width=50, bg="#bbbbbb")
lblChat.pack(side=TOP)
txtInput = Entry(main,  width=40, textvariable=strInput)
txtInput.pack( side = LEFT)
cmdSubmit = Button(main, width=10, command=submit, text="Submit")
cmdSubmit.pack(side=RIGHT)
main.mainloop()
