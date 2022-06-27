#Lexicographical order -----> dictionary order

# def sortlexo(mystr):
#     words = mystr.split()
#     words.sort()
#     st = set(words)     # here i have also converted the list in set so that we don't get the duplicate values (this is unncessary)
#     for i in st:
#         print(i)

# sortlexo(input("Enter the sentence : "))

#-----------------------------------alternate method-----------------------------------#method1

# print("Enter the name of the city")
# a,b,c = input(),input(),input()
# x = min(a,b,c)
# print(x)
# if x==a:
#     print(min(b,c),max(b,c))
# elif x==b:
#     print(min(a,c),max(a,c))
# else:
#     print()
#     print(min(a,b),max(a,b))

#-----------------------------------alternate method with list comprehension-----------------------------------#method1

[i for i in sorted(input("Enter comma separated three city names").split(',')) if print(i, end=' ')]