from numpy import *
m = int(input("Enter the no of rows:"))
n = int(input("Enter the no of columns:"))
a = zeros((m,n),dtype=int)
print(a)
u = len(a)


for i in range(u):
    for j in range(len(a[i])):
        x = int(input("Enter element:"))
        a[i][j] = x

#WITH INDEX

for i in range(u):
    for j in range(len(a[i])):
        print(a[i][j])

print(a)

#WITHOUT INDEX

for r in a:
    for c in r:
        print(c)
print(a)