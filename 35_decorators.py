# def function1():
#     print("Subscribe now")

# func2 = function1()
# del function1
# func2
# print(func2)


# def funcret():
#     print("Choose from 0 or 1")
#     num = int(input())
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a = funcret()
# print(a)

# def executor(func):             # returning function as an argument
#     func("this")
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")  
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_harry():
    print("Harry")

# who_is_harry = dec1(who_is_harry)

who_is_harry()


# def prints(func):
#     print("Executing Now")
#     func()
#     print("Executed")


# def sums(a,b):
#     c = a+b
#     print(c)

# a = int(input("Enter the first no"))
# b = int(input("Enter the second no"))
# sums(a,b)

# def dec(func2):
#     def nowexec():
#         print("now exec")
#         func2()
#         print("executed")
#     # return nowexec

# def a():
#     print("i am abhay")

# a = dec(a)
# a()

# Python program to illustrate functions
# can be treated as objects
# def shout(text):
# 	return text.upper()

# print(shout('Hello'))

# yell = shout

# print(yell('Hello'))


# Python program to illustrate functions
# can be passed as arguments to other functions

def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func1):
    # storing the function in a variable
    greeting = func1("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)



# Python program to illustrate functions
# Functions can return another function
 
# def create_adder(x):
#     def adder(y):
#         return x+y
 
#     return adder
 
# add_15 = create_adder(15)
 
# print(add_15(10))


                #MULTIPLY DECORATOR FUNCTION

def multiply_decorator(function):
    def inner():
        x = function()
        a = x*x
        return a
    return inner

def multiply1_decorator(function):
    def inner():
        x = function()
        a = 2*x
        return a
    return inner

@multiply_decorator
@multiply1_decorator 
def number():
    return 10
print(number())