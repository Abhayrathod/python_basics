from concurrent.futures import thread
from threading import Thread, current_thread

# def dis():
#     print("default chlid thread name", current_thread().name)
#     current_thread().name = "new child thread"
#     print("default chlid thread name",current_thread().name)

# t = Thread(target= dis)
# t.start()
# print(t.name)

# print("Default main thread name", current_thread().name)
# current_thread().name = "new main thread"
# print("default main thread name",current_thread().name)

#another way to set and get name of thread

def dis():
    pass

t = Thread(target= dis)
t.start()
print(current_thread().name)
current_thread().name = "new main thread"
print(current_thread().name)
print("default", t.name)
t.name = "newly created"
print(t.name)