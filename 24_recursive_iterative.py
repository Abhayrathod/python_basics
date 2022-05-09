# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!

# def factorial_iterative(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac


# def factorial_recursive(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     if n ==1 or n ==0:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)

                # 5 * factorial_recursive(4)
                # 5 * 4 * factorial_recursive(3)
                # 5 * 4 * 3 * factorial_recursive(2)
                # 5 * 4 * 3 * 2 * factorial_recursive(1)
                # 5 * 4 * 3 * 2 * 1 = 120

# # 0 1 1 2 3 5 8 13
# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# number = int(input("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(4))
# print("Factorial Using Recursive Method", factorial_recursive(4))
# print(fibonacci(3))
  



# -----------------Python3 program to find factorial of given number--------------------

# ----- Recursion -----
# ------------method to find factorial of given number
# def factorialUsingRecursion(n):
# 	if (n == 0):
# 		return 1

# 	# recursion call
# 	return n * factorialUsingRecursion(n - 1)

# ----- Iteration -----
# ----------Method to find the factorial of a given number
# def factorialUsingIteration(n):
# 	res = 1

# 	# using iteration
# 	for i in range(2, n + 1):
# 		res *= i

# 	return res
# num = 5
# print("Factorial of",num,"using Recursion is:",
# 					factorialUsingRecursion(5))

# print("Factorial of",num,"using Iteration is:",
# 					factorialUsingIteration(5))





# -------------------A Python 3 program to demonstrate working of recursion----------------------
# def printFun(test):

# 	if (test < 1):
# 		return
# 	else:

# 		print(test, end=" ")
# 		printFun(test-1) # statement 2
# 		print(test, end=" ")
# 		return
# test = 3
# printFun(test)


#------------ A Python 3 program to demonstrate working of recursion------------------
#-------------Python code to implement Fibonacci series Function for fibonacci-----------------------
# def fib(n):

# 	# Stop condition
# 	if (n == 0):
# 		return 0

# 	# Stop condition
# 	if (n == 1 or n == 2):
# 		return 1

# 	# Recursion function
# 	else:
# 		return (fib(n - 1) + fib(n - 2))

# n = 5
# print("Fibonacci series of 5 numbers is :",end=" ")

# # for loop to print the fibonacci series.
# for i in range(0,n):
# 	print(fib(i),end=" ")


#--------practise question 1
# def fun(x,y):
#     if x==0:
#         return y
#     else:
#         return fun(x-1,x+y)

# print(fun(4,5))

#--------practise question 2
# Minimum index finder
def minIndex(arr, s, e):
	
	sml = sys.maxsize
	mindex = 0
	
	for i in range(s, e):
		if (sml > arr[i]):
			sml = arr[i]
			mindex = i
			
	return mindex

def fun2(arr, start_index, end_index):
	
	if (start_index >= end_index):
		return
		
	# minIndex() returns index of minimum value in array arr[start_index...end_index]
	min_index = minIndex(arr, start_index, end_index)
	arr[start_index], arr[min_index] = arr[min_index], arr[start_index]
	fun2(arr, start_index + 1, end_index)