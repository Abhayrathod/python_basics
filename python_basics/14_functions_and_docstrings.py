# a = 9
# b = 8
# c = sum((a, b)) # built in function

# def function1(a, b):
#     print("Hello you are in function 1", a+b)
#     return(a+b)
# def function2(a, b):
#     """This is a function which will calculate average of two numbers
#     this function doesnt work for three numbers"""
#     average = (a+b)/2
#     #print(average)
#     return average

# v = function2(5, 7)
# print(v)
# print(function2.__doc__)
# c = function1(3,4)
# print(c)
# print(function1(3,4))



# returning two values from function

# def add_sub(x,y):
#     a = x + y
#     b = x - y
#     return a,b

# sum,sub = add_sub(40,50)
# print(sum,sub)

#nested funtion

# def disp(a):
#     def show():
#         return "show function"
#     result = show() + a + "disp function"
#     return print(result)
    # return result
# a = disp("abhay")
# print(a)
#or    
# print(disp("abhay"))

#passing a function as a paramenter

# def dispp(sh):
#     print("disp function " + sh)
# def show():
#     return "show function"

# dispp(show())   #yaha bhulna mat ki mene function k argument me paranthesis laga k pass kiya hai tabhi vo
#                 #execute hua hai nahi to fir jaha print me "sh" likha hua hai uske aage paranthesis lagana 
                #padta , tabhi function chlta bina paranthesis k nahi chlega

                        #function returning as another function

# def display():
#     def show():
#         return "show function"   # AGAR YAHA PAR PRINT LIKHE OR RETURN NAHI LIKHE TO PHIR OUTPUT ME NONE PRINT 
#                                  # HOGA KYUKI TAB SHOW FUNCTION NE KUCH RETURN NAHI KIYA HOGA BAS PRINT KARKE 
#                                  # CHHOD DIYA HOGA
#     print("display function")
#     return show
# a = display()
# print(a())

# ab isi me funtion ko as a paramenter pass kar rahe hai

# def display(sh):
#     print ("display function")
#     return sh
# def show():
#     return "show funtion"

# a = display(show)
# print(a())


#---------------------------geeky shows 
# def add(x,y):
#     print("the sum of the two value is :",x+y)

# a = float(input("enter the first value"))
# b = int(input("enter the second value"))
# add(a,b)
#------------
# def add(y):
#     x = 10
#     c = x+y
#     return c

# sum = add(20)
# print(sum)

#-----------------returning two values
# def calc(x,y):
#     a = x+y
#     b = x-y
#     return (a,b)
# x,y = calc(34,34)
# print(x,y)

#--------------------nested functions
# def disp():
#     def show():
#         return "this is show function"
#     result = show() +" "+ "disp function"
#     return result
# a = disp()
# print(a)

#-------------------passing fucntion as a parameter
# def disp(sh):
#     return "disp " + sh()
# def show():
#     return "show"
# a = disp(show)
# print(a)

#----------------functions returning another function

# def disp():
#     def show():
#         return"show"
#     print("disp")
#     return show

# a = disp()
# print(a())

#----OR
#-yaha pr function ko andar nahi likha hai

# def disp(sh):
#     print("disp")
#     return sh
# def show():
#     return"show"
# a = disp(show)
# print(a())

#------------------------formal and actual arguments

#------------positional argument

# def add(x,y):
#     z = x+y
#     print(z)
# add(4,5)

#---------keyword arguments

# def show(name,age):
    # print(name,age)
# show(name="abhay",age=25)
# show(age=25,name="abhay")``
# show(25,"abhay")

#---------default arguments

# def show(name,age=25):
    # print(name,age)
# show("abhay",age=20)  #jab default ki jagah actual argument dete hai to actual vale ki priority jyada hoti hai
# show("abhay")

#-----variable length argument

# def show(x,*num):
#     print (num[0])
#     print (num[1])
#     print (num[2])
#     z = x + num[0] + num[1] + num[2]
    # print(z)
# show(2,3,4)
# show(1,2,3,4,5,6,7,8,9,0)   #yaha par bhale kitne argument do ,error nahi aayegi

#------keyword variable length argument

# def add(x,**num):
#     z = x + num['a'] + num['b'] + num['c']
#     print(z)
# add(2,a=3,b=4,c=5, d=12 , e=14)     #yaha pr do argument jyada diya hai lekin ise koi farq nahi padta

#--------------lambda function

# add = lambda x,y : x+y
# a = add(5,6)
# print(a)

#---another way
# add_sub = lambda x,y : (x+y,x-y)
# a,b = add_sub(8,9)
# print(a)
# print(b)

#----------------nested lambda function

# add = lambda x = 10 : (lambda y:x+y)
# a = add()
# print(a(4))

#--------------------passisng lambda function to another function

# def show(a):
#     print(a(4))

# show(lambda x:x)

#---------------------returning lambda from a function

# def add():
#     y = 20
#     return (lambda x:x+y)
# a = add()
# print(a(10))

#-------------------immediately invoked function in python

# (lambda x,y: print(x+y))(6,8)