# a = 'geeks for geeks'
# print(set(a.split(' ',2)))



#----------------list comprehension-------------
# lst = []
# for i in range(100):
#     if i%3 ==0:
#         lst.append(i)
# print(lst)

# lst = [i for i in range(100) if i%3==0] #this is list comprehension in python
# print(lst)

# lst= [int(input("Enter the numbers").split(','))]
# for i in lst:
#     if i%2 ==0:
#         print(str(i),"the number is even")
#     else:
#         print(str(i),"the number is odd"). /


# iter_list = iter([input("Enter the characters").split('-')])
# iter_list = iter([input("Enter the characters").split('-')])
# print((next(iter_list)))
# print((next(iter_list)))


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

#-------------------method 1-------
# ans = [[i,j,k] for i in range(0,x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
# print(ans)
#-------------------method 2-------
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 print([i,j,k],end='')


# n1 = [1,2,3]
# n2 = [4,5,6]
# result = map(lambda x,y:x+y,n1,n2)

<<<<<<< HEAD

import random
import string

print(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
)
=======
#---------------------------------------------------


# def func(fun):

#     def inn_fa():
#         print("this is before the func execution")
#         fun()
#         print("this is after func execution")
#     return inn_fa

# def p_func():
#     print("this is inside func")
# var = func(p_func)
# var()


import uuid
a = uuid()
print(a)
>>>>>>> af653441e1a88e56701bffeca7e06dfead464ee6
