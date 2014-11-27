# from mt_client import ChatClient
# from gui import *
from reciever import Reciever
from sender import Sender
from multiprocessing.pool import ThreadPool
from gui import ChatGui

reciever = Reciever()
sender = Sender()
gui = ChatGui(sender)

while True:
    pool = ThreadPool(processes=1)
    reciever_result = pool.apply_async(reciever.recieve_data())
    reciever_return_val = reciever_result.get()
    print("recieved data")
    print(reciever_return_val)
    gui.writeLine(reciever_return_val)
    #threading.Thread(target=reciever.recieve_data(), args = ()).start()










