                           #FIBONACCI SEQUENCE

# print("Fibonacci sequence: ")
# nterms = int(input("Please enter the term for which you want to print fibonacci sequence"))
# count = 0
# n1 =0
# n2 = 1
# while count < nterms:
#     print (n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1
                  #OR      # fibonacci as a function
# def fibo(nt):
#     n1 = 0
#     n2 = 1
#     count = 0
#     while count<nt:
#         print(n1)
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         count+=1

# fibo(int(input("Enter the terms up to which you want to print fibonacci no")))  


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


                           # PRINTING ID OF NO IN RAM MEMORY

# a=2
# print('id(2) = ',id(2))
# print('id(a) = ',id(a))
# a= a+1
# print('id(3)=',id(3))
# b =2 
# print('id(2)',id(2))

# str = "ts is ng le"
# a = dict(str.split())
# del a['t']


                            # PALINDROME CHECK 

# a = str(input("Enter the string for palindrome verification: "))
# def ispalindrome(a):
#     for i in range(0,int(len(a)/2)):
#         if a[i] != a[len(a)-i-1]:
#             return False
#     return True

# if ispalindrome(a):
#     print("yes")
# else:
#     print("no")