from numpy import *

n = int(input("Enter the no of elements: "))
a = zeros(n, dtype= int)

u = len(a)
i = 0

while i<u:
    x = int(input("Enter the elements: "))
    a[i] = x
    i += 1

print(a)