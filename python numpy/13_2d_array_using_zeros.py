from numpy import *
a = zeros((3,2), dtype=int)
print(a)

#WITHOUT INDEX

# for r in a:
#     for c in r:
#         print(c)
#     print()

#WITH INDEX

# n = len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print('index', i , j , " = ", a[i][j])
#     print()

#USING WHILE LOOP

n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print('index',i,j,"=", a[i][j])
        j+=1
    i+=1
    print()