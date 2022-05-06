# lambda is a one liner function also called anonymous function


# minus = lambda x, y :x-y
# print(minus(8,5))


            #SORTING OUT WITH LAMBDA

# def a_first(a):
#     return a[1]

# a = [[1,4], [5,56], [8,23]]
# a.sort(key=a_first)

# a.sort(key=lambda x:x[1])
# print(a)

            #SQUARE FUNCTON WITH LAMBDA

# b = lambda x: x*x*x
# print(b(7))

# def power(n):
#     return lambda x: x**n
# base = power(2)
# print(base(8))


# a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]
# in filter either we use assignment or conditional operator, the pass actualbparameter will get return
# filtered = filter (lambda x: x % 2 == 0, a)
# print(list(filtered))


# in map either we use assignment or conditional operator, the result of the value will get returned
# mapped = map (lambda x: x % 2 == 0, a)
# print(list(mapped))


# ITERATING BY PYTHON LAMBDAS
# l1=[86,6,3,8,9]
# l2=[]
# for i in l1:
#     temp = lambda i:i**2
#     l2.append(temp(i))
# print(l2)

#ITERATING BY PYTHON LAMBDAS USING MAP FUNCTION
# l1 = [4,2,13,21,5]
# l2 = list(map(lambda v:v**2,l1))
# print(l2)


#ITERATING WITH PYTHON LAMBDAS AND USING FILTER
# l1 = [4,2,14,21,5]
# l2 = list(map(lambda v: v**2, filter(lambda u:u%2,l1)))
# print(l2)


# Python program to demonstrate lambda functions
# x ="GeeksforGeeks"
# # lambda gets pass to print
# (lambda x : print(x))(x)


#Python Lambda Function with List Comprehension
# tables = [lambda x=x: x*10 for x in range(1, 11)]
# for table in tables:
#     print(table())


# Example of lambda function using if-else
# Max = lambda a, b : a if(a > b) else b
# print(Max(1, 2))
# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
# # Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)


#Python Lambda with Multiple statements
# Get the second largest element
# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
# # Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)
# # Get the second largest element
# secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
# res = secondLargest(List, sortList)
# print(res)


# Using lambda() Function with filter() Python code to illustrate filter() with lambda()
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: (x%2 != 0) , li))
# print(final_list)


# Python 3 code to people above 18 yrs
# ages = [13, 90, 17, 59, 21, 60, 5]
# adults = list(filter(lambda age: age>18, ages))
# print(adults)


# Python code to illustrate map() with lambda() to get double of a list.
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(map(lambda x: x*2, li))
# print(final_list)


# Python program to demonstrate use of lambda() function  with map() function
# animals = ['dog', 'cat', 'parrot', 'rabbit']
# #here we intend to change all animal names to upper case and return the same
# uppered_animals = list(map(lambda animal: str.upper(animal), animals))
# print(uppered_animals)


# Python code to illustrate reduce() with lambda() to get sum of a list
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print (sum)

# # python code to demonstrate working of reduce() with a lambda function
# # importing functools for reduce()
# import functools
# # initializing list
# lis = [ 1 , 3, 5, 6, 2, ]
# # using reduce to compute maximum element from list
# print ("The maximum element of the list is : ",end="")
# print (functools.reduce(lambda a,b : a if a > b else b,lis))
