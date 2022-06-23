#--------------------------MAP------------------------------
# numbers = ["3", "34", "64"]
# numbers = list(map(int, numbers))
# numbers[2] = int(numbers[2]) +1
# # print(numbers)

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     print(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a

# num = [2,3,5,6,76,3,3,2]
# square = list(map(sq, num))
# print(square)
#-----------using lambda
# num = [2,3,5,6,76,3,3,2]
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square, cube]
# num = [2,3,5,6,76,3,3,2]
# for i in range(len(num)):
#     # val = list(map(lambda x:x(i), func))
#     val = list(map(square, num))
#     valu = list(map(cube, num))
#     print(val[i],valu[i])

#DOUBLE THE NUMBERS USING MAP FUNCTION---------------
# def addition(n):
#     return n * n

# numbers = (1,2,3,4)
# result = list(map(addition, numbers))
# result = list(map(lambda x: x*x, numbers))
# print(result)

#ADDING TWO LIST USING LAMBDA-------------------------

# numbers1 = [1,2,3,4]
# numbers2 = [4,5,6]
# result = list(map(lambda x,y: x+y,numbers1,numbers2))
# print(result)

#LISTING STRINGS INDIVIDUALLY-------------------------

# l = ['abhay','asnjv','sbhsbs','bvlbv']
# test = list(map(list,l))
# print(test)

#--------------------------FILTER------------------------------
# list_1 = [1,2,3,4,5,6,7,8,9]

# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)

#-------------another question
# def check_vowel(vari):
#     num1 = ['a','e','i','o','u']
#     if vari in num1:
#         return True
#     else:
#         return False
# # this = str(input("Enter the strings you want to check"))
# # print(check_vowel(this))
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# filtered = filter(check_vowel,sequence)
# print("The filtered letters are:")
# for s in filtered:
#     print(s)
# #--------------------------REDUCE------------------------------
# from functools import reduce

# list1 = [1,2,3,4,2]
# num = reduce(lambda x,y:x*y, list1)
# # num = 0
# # for i in list1:
# #     num = num + i
# print(num)

# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(reduce(lambda a, b: a if a > b else b, list1))