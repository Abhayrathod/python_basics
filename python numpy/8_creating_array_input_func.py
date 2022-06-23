from numpy import *

n = int(input("Enter the Number of elements you want to create the array of: "))
a = zeros(n,dtype = int)

for i in range(len(a)):
    x = int(input("Enter elements"))
    a[i] = x
print(a)

for i in range(len(a)):
    print("a[",i,"] = ",a[i])
