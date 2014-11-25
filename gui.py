from tkinter import *

main = Tk()
strInput = str()
lblChat = Label(main, height=100, width=150, bg="grey")
lblChat.pack(side=TOP)
txtInput = Entry(main, textvariable=strInput)
txtInput.pack( side = LEFT)
main.mainloop()
