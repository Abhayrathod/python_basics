from numpy import *

# any() and all() are built-in function in python

arr1 = array([100,200,300,400,500])
arr2 = array([100,200,300,400,500])

# any() - this function returns true if any one variable of the iterable is true ,\
#     then it will return false

c = arr1==arr2
print(c)
print(any(c))


#all() - this fuction returns true if all the elements of the iterable is true or if iterable is empty

print(all(c))