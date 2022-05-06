from time import sleep
from threading import Thread, Event

def light_switch():
    sleep(2)
    e.set()
    print("Green Light is on")
    sleep(1)
    e.clear()
    print("Red light is on now")

def vehicle():
    e.wait()
    while e.is_set():
        print("Go")
    print("Program done")

e = Event()

t1 = Thread(target=light_switch)
t2 = Thread(target=vehicle)
t1.start()
t2.start()