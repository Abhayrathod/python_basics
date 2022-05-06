def some_func():
    print("Inside some_func")
    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:",var)
    some_inner_func()
    print(id(some_inner_func))
    # print("Try printing var from outer function: ",var)
c = some_func()
print(id(some_func))