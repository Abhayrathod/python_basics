                            # REVERSING NO WITHOUT USING ANY FUNCTION

# list1 = [1, 2, 3, 4, 5]
# L = len(list1)
# for i in range(int(L / 2)):
#     n = list1[i]
#     list1[i] = list1[L - i - 1]
#     list1[L - i - 1] = n
# print(list1)

#         # OR

# def reverse_list(list2):
#     l = len(list2)
#     for i in range(int(l/2)):
#         n = list2[i]
#         list2[i] = list2[l-i-1]
#         list2[l-i-1] = n
#     print(list2)

# n = reverse_list([1,2,3,4,5])


                            # REVERSING LIST USING SOME BUILT IN FUNCTOINS

# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list2.reverse()
# l = len(list2)
# for i in range(l):
#     list1[i] = list2[i]
# del list2
# print(list1)


                            # SORTING AND REVERSING RANDOM NO WITHOUT USING FUNCTION

# number=[1,5,6,9,0]
# for i in range(len(number)):
#   for j in range(i+1,len(number)):
#     if number[i]<number[j]:
#       number[i],number[j]=number[j],number[i]
# print(number)

    #ANOTHER METHOD BY TAKING INPUT FROM USER

# n = int(input("Enter the terms:"))
# list1 = []

# for i in range(0,n):
#     print("Enter the element:{}".format(i+1))
#     element = int(input())
#     list1.append(element)
# print("The entered list is:",list1)

# L = len(list1)

# for j in range(L):
#     for k in range(j+1,L):
#         if list1[j]>list1[k]:
#             list1[j],list1[k] = list1[k],list1[j]
# print("The sorted list in ascending order is:",list1)