from numpy import *

a = array([[10,20,30,40,50],[60,70,80,90,100]])


                #without index
# for r in a:
#     for c in r:
#         print(c)
#     print()

                #with index

n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print()