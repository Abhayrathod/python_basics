from array import *

stud_roll = array('i',[101,102,104,108])        # here 'i' is for indicating that array will be of integer type
print (stud_roll)
# stud_roll.append(106)
print(stud_roll[3])
# stud_roll.remove(106)
# print(stud_roll[3])

#USING FOR LOOP

# for el in stud_roll:
#     print(el)

# making new list and inserting values using for loop
# lst = []
# for i in stud_roll:
#     lst.append(i)
# print(lst)

#USING FOR LOOP

# n = len(stud_roll)
# # print(n)
# for i in range(n):
#     print(stud_roll[i])

#USING WHILE LOOP IN PYT
# i=0
# n = len(stud_roll)
# while (i<n):
#     print(stud_roll[i])
#     i+=1

#APPENDING INTO ARRAY

# new_roll = array('i',[])
# a  = int(input("Enter the no of items you want to create in array"))

# # # using while loop
# b=0
# while (b<a):
#     c = int(input())
#     new_roll.append(c)
#     print(new_roll)
#     b +=1

# # using for loop
# for i in range(a):
#     c = int(input())
#     new_roll.append(c)
#     print(new_roll)

#ANOTHER METHOD TO APPEND INTO ARRAY

# my_roll = array('i',[])
# n = int(input("how many elements?"))
# for i in range(n):
#     my_roll.append(int(input("Enter the elements")))
# for i in range(len(my_roll)):
#     print(my_roll[i])
# print(my_roll)