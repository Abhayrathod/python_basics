#two types of multitasking - 1 process based multitasking - processed are independent
                            # 2 thread based multitasking - thread are part of the same process 


# WAYS OF CREATING THREAD -   1 CREATING A THREAD WITHOUT Class
                            # 2 CREATNG A THREAD BY CREATING A CHILD CLASS TO THREAD Class
                            # 3 CREATING A THREAD WITHOUT CREATING CHILD CLASS TO THREAD CLASS


                        
                        
                        # 1 CREATING A THREAD WITHOUT Class
# SYNTAX - Thread(target=function, args = 1,2,....)


from threading import Thread, current_thread
import threading


# t = threading.current_thread().name
# print("abhay")
# print(t)

# def disp():
#     for i in range(5):
#         a = current_thread().getName
#         print(a)
#         print("child thread", current_thread().name)

# t = Thread(target= disp)
# t1 = Thread(target= disp)
# t.start()
# t1.start()
# for i in range(5):
#     print("main thread",current_thread().name)


                        # 2 CREATNG A THREAD BY CREATING A CHILD CLASS TO THREAD Class

# class mythread(Thread):
#     def run(self):
#         for i in range(5):
#             print("child thread")

# t = mythread()
# t.start()
# for i in range(5):
#     print("main thread")

                        # CREATING A THREAD CHILD CLASS WITH CONSTRUCTOR

# class mythread(Thread):
#     def __init__(self,a):
#         Thread.__init__(self)
#         print("child  thread constructor",a)

#     def run(self):
#         pass

# t = mythread(10)
# t.start()
# print(current_thread().name)


                        # 3 CREATING A THREAD WITHOUT CREATING CHILD CLASS TO THREAD CLASS

# class mythread:
#     def disp(self,a,b):
#         print(a,b)

# myt = mythread()

# t = Thread(target=myt.disp, args=(10,20))
# t.start()