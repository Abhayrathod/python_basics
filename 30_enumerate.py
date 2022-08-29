# l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"] 

# # i = 1
# # for item in l1:
# #     if i%2 is not 0:
# #         print(f"Jarvis please buy {item}")
# #     i += 1

# for index, item in enumerate(l1):
#     if index%2==0:
#         print(f"Jarvis please buy {item}")




# python
# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
print(list(enumerate(l1)))
# # creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)

# print ("Return type:", type(obj1))
# print (list(enumerate(l1)))

# # changing start index to 2 from 0
# print (list(enumerate(s1, 2)))

# for i,j in obj1:
# 	print(i,j)



# Python program to illustrate enumerate function in loops
# l1 = ["eat", "sleep", "repeat"]
# new = enumerate(l1)
# print(tuple(new))
# printing the tuples in object directly
# for ele in enumerate(l1):
# 	print (ele)

# changing index and printing separately
# for count, ele in enumerate(l1, 100):
# for count, ele in enumerate(l1, int(input())):
	# print (count, ele)

# getting desired output from tuple
# for count, ele in enumerate(l1):
# 	print(count)
# 	print(ele)
