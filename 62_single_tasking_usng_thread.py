from threading import Thread
from time import sleep
import time


class exam:
    def solve_questions(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("q1 solved")
        # time.sleep(3)
    def q2(self):
        print("q2 solved")
        # sleep(3)
    def q3(self):
        print("q3 solved")

e = exam()
t = Thread(target=e.solve_questions)
t.start()