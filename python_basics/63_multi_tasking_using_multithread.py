from threading import Thread

class hotel:
    def __init__(self,t):
        self.t = t

    def food(self):
        for i in range(1,6):
            print(self.t,i)

h1 = hotel("take order from table")
h2 = hotel("serve order from table")

t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)
t1.start()
t2.start()