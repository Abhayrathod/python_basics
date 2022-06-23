from numpy import *


# COMPARING ARRAYS USING NUMPY

a = array([100,200,300,400,500])
b = array([100,200,3,4,500])
c = a==b
# c = a<b
# c = a>b
# c = a>b
print(c)


# ADDING TWO ARRAY
roll = array([101,102,103,104,105])
r = array([1,2,3,4,5])
c = roll + r
print(c)

for el in c:
    print(el)