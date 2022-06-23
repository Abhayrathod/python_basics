# def gen():
#     n=1
#     print("this is printed first")
#     yield n
#     n+=1
#     print("this is printed second")
#     yield n
#     n+=1
#     print("this is printed third")
#     yield n
# a = gen()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

#----------------fibonaaci using generator funcition-------------------------
def fib(limit):
	a, b = 0, 1
	while a < limit:
		yield a
		a, b = b, a + b

# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.__next__()) # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating over the generator object using for
# in loop.
# print("\nUsing for in loop")
# for i in fib(5):
# 	print(i)
