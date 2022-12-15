#SEMAPHORE
from ast import arg
from ctypes.wintypes import tagRECT
from threading import *
import threading

class Booking:
    def __init__(self,available_seats):
        self.available = available_seats
        self.l = BoundedSemaphore(2)
        print(self.l)

    def book(self,need_seat):
        self.l.acquire()
        self.l.acquire()
        print(self.l._value)
        print("Available seats:", self.available)
        if (self.available>=need_seat):
            name = current_thread().name
            print(f"{need_seat} is alloted to {name}")
            self.available-= need_seat
        else:
            print("Sorry! All seats has been alloted")
        self.l.release()
        self.l.release()

f = Booking(2)
t1 = Thread(target=f.book,args=(1,), name = "abhay1")
t2 = Thread(target=f.book,args=(1,), name = "abhay2")
t3 = Thread(target=f.book,args=(1,), name = "abhay3")
t1.start()
t2.start()
t3.start()
print("Main Thread")