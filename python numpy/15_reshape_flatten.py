#reshape function - This function is used to change the shape of array. We can convert 1D array to 2D or 3D
# array and vice versa. The new array should have the same number of elements as in original array.

#syntax - reshape(array_name, (n,r,c))
# array_name - It represents the no of array in the resultant array
# n - n is the number of arrays in the resultant array
# r - r is the number of rows
# c - c is the number of columns

from numpy import *
a = array([1,2,3,4,5,6,7,8,9,10,11,12])
b = reshape(a,(2,2,3))
print(a)
print(b)

e = array([[1,2,3],[4,5,6]])
f = reshape(e,6)
print(f)

#flatten - The flatten method is used to convert 2d or 3d array to 1d array. 

#syntax - array_name.flatten()

e = array([[1,2,3],[4,5,6]])
f = e.flatten()
print(f)