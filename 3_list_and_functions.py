# list1 = ['harry', 'ram', 'Aakash', 'shyam', 5, 4.85]

#                     #    Lists in Python

# []                                             # list with no member, empty list
# [1, 2, 3]                                    # list of integers 
# [1, 2.5, 3.7, 9]                           # list of numbers (integers and floating point)
# ['a', 'b', 'c']                               # list of characters
# ['a', 1, 'b', 3.5, 'zero']                # list of mixed value types
# ['One', 'Two', 'Three']               # list of strings 

# # List Methods :
# l1=[1,8,4,3,15,20,25,89,65]       #l1 is a list
# print(l1) 

# l1.sort()
# print(l1)      #l1 after sorting
# l1.reverse()
# print(l1)      #l1 after reversing all elements, dont reverse first and then sort beacause it will sort the reversed list


# # seq = list1[start_index:stop_index]

# # List Methods :- 
# list1=[1,2,3,6,5,4]     #list1 is a list

# list1.append(7)    # This will add 7 in the last of list 
# list1.insert(3,8)    # This will add 8 at 3 index in list
# list1.remove(1)    #This will remove 1 from the list 
# list1.pop(2)          #This will delete and return index 2 value.
# print(list1)


# # Tuples in Python :


# a=()    # It's an example of empty tuple
# x=(1,)   # Tuple with single value i.e. 1 
# tup1 = (1,2,3,4,5)
# tup1 = ('harry', 5, 'demo', 5.8)

# # Swapping of two numbers :
# a = 10 
# b = 15
# print(a,b)     #It will give output as: 10 15
# a,b = b,a 
# print(a,b)     #It will give output as: 15 10

# grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",
#            "Lollypop", 56]
# print(grocery[5])
# numbers = [2, 7, 9, 11, 3, 6, 8, 10, 16, 17, 18, 15, 13, 32]
# print(numbers[-8:-3])
# numbers.remove(9)
# numbers.pop(3)
# numbers.sort()
# numbers = []
# numbers.reverse()
# numbers.append(1)
# numbers.append(72)
# numbers.append(5)
# numbers.insert(2, 67)
# 3, 11, 9, 7, 2
# print(numbers)
# numbers[2] = 98
# print(numbers)
# # Mutable - can change
# # Immutable - cannot change
# tp = (1,)
# print(tp)



# swapping two numbers using a third varialble
# a = 1
# b = 8
# temp = a
# a = b
# b = temp
# print(a, b)

# l5=['apple', 'apple', 'banana', 'banana']
# print(l5*2)
# print(l5[2:5])
# l5.append('abhay')
# l5.remove('banana')
# l5.pop(0)
# # l5.clear()
# print(l5.index('apple'))
# l5.extend('dhch')
# l5.reverse()
# l5.insert(1,34)
# print(l5)
# l4 = l5.copy()
# print(l4)
# l3 = l5[0]
# print(l3)
# if "apple" in l5:
#     print("yes")


# thistuple = ('apple', 'mango', 'banana', 34, 54, 24 ,78, 54)
# a = thistuple[0]
# print(a) 
# print(thistuple[2:5])
# print(thistuple[2:50])
# print(thistuple[2:])
# print(thistuple[4:-1])
# if 'apple' in thistuple:
#     print("yes")

# y = list(thistuple)
# y[1] = 'new'
# print(y)
# y.append("abhay")
# thistuple = tuple(y)
# print(thistuple)
# print(type(thistuple))


#adding two tuples

# y = ("newtuple",)
# thistuple += y
# print(thistuple)

# items = ('new', 'old', 'plane', 'bike','taxi','new')
# (a,b,*c,d) = items
# print(a)
# print(b)
# print(c)
# print(d)
# print(items*2)
# print(items.index('bike'))
# print(items.count('new'))


#-----------------convert list to dictionary-------------––––––––––––––––––––
# lst = ['a', 1, 'b', 2, 'c', 3]
# def convert_to_dict(lst):
#     res_dct = {lst[i]:lst[i+1] for i in range(0,len(lst),2)}
#     return res_dct
# print(convert_to_dict(lst))

#----------------------------list comprehsion------------------------------
# lst = [i for i in range(100) if i%3==0]
# print(lst)