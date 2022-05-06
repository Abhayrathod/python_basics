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