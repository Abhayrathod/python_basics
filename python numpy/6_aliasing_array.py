# Aliasing means to give anther name to exixting object. It doesnt mean copying

from numpy import *

a = array([100,200,300,400,500])
b = a
print (a)
print (b)
print("a: ", id(a))
print("b :", id(b))