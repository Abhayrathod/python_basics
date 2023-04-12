# def function_name_print(a,b,c,d):
    # print(a,b,c,d)
# function_name_print("anjdcj", "dcnjc", "dsjcdb", "dcjd")

#--------------python program for args and kwargs
def funargs(normal,*args,**kwargs):
    print(normal)
    print(type(args))
    print(type(kwargs))
    print(args[4])
    for items in args:
        print(items)
    print("now i will introduce some random stuff")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
normal = ("this is me")
kw = {"abhay":"programmer", "abc":"newtown","bcd":"def","cde":"efg"}
ab = ["dc", "dnbchjd", "dcbhjdsbc", "ndcjbdhc", "dcbhjsdvc"]
funargs(normal, *ab, **kw)


#--------------Python program to illustrate *args for variable number of arguments
# def myFun(*argv):
# 	for arg in argv:
# 		print (arg)
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#---------------printing first argument thorugh argument 
# def myfun(argv1, *args):
#     print("First argument: ", argv1)
#     for args in args:
#         print("next item printing through args: ",args)
# myfun("hello", "this",'is','abhay')

# def myfun1(**kwargs):
#    for key, value in kwargs.items():
#        print("%s ==  %s" %(key,value))
# myfun1(first="lol", second="lol",third="lol")

# def myfun1(argv1,**kwargs):
#     print(argv1)
#     for key, value in kwargs.items():
#         print("%s ==  %s" %(key,value))
# myfun1("hi",first="lol", second="lol",third="lol")

# def fun(arg1,arg2,arg3):
#     print("arg1",arg1)
#     print("arg2",arg2)
#     print("arg3",arg3)
# # args = ("geeks","for","geeks")
# # fun(*args)
# kwargs = {"arg1":"geeks","arg2":"for","arg3":'geeks'}
# fun(**kwargs)