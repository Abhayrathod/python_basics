# view() - This method is used to construct a new view of array with same data of existing array. \
    # This existing array and new array will shar different memory locations. \
    # If the new array get modified then exising array will also be modified as the element in both the array \
        # will be like mirror image

from numpy import *

# a = array([100,200,300,400,500])
# b = a.view()
# b[2] = 1000         #This changes both the array
# print(a)
# print(b)
# print("id(a) :", id(a))
# print("id(b) :", id(b))

# copy() - This method is used to create  a copy of an existing array. If the new array gets modified ,\
    # the exisiting array will not be affected

aa = array([100,200,300,400,500])
bb = aa.copy()
bb[2] = 1000                #This does not change the array from which this has been copied
print(aa)
print(bb)
print("id(a) :", id(aa))
print("id(b) :", id(bb))