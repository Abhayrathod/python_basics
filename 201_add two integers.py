# a = int(input("Enter the 1st no"))
# b = int(input("Enter the second no"))
# c = [a,b]
# print(sum(c))  #sum function takes list as a argument and sum all the no in the list.
# print(sum(c,50))  # sum(iterable,start) sum function takes list,dict,tuple as argument and takes start - which is added to the sum

#-------------------sum fucntion with dictionary-------------------

# dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
# print(type(dict1.values()))  # this will return type as dict_values object , values is inbuilt method in/
                                    # python and it returns view object and view object contains the values of the dictionary as a list.
# print(sum(dict1.values()))

#-------------------sum function with tuple------------------------

tp = (1,2,3,4,5,6,7,8,9)
print(sum(tp))