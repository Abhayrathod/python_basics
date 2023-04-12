#find three largest elements in the array 


#-------------------------------
# time complexity O(logn)
# Auxiliary Space: O(1)

# import sys

# def printlargest(arr, arr_size):

#     if (arr_size < 3):
#         print("Invalid Input")
#         return

#     third = second = first = -sys.maxsize

#     for i in range(0,arr_size):

#         if (arr[i]> first):

#             third = second
#             second = first
#             first = arr[i]
        
#         elif (arr[i]> second):

#             third = second
#             second = arr[i]

#         elif (arr[i]> third):

#             third = arr[i]
    
#     print("Three largest elements in the array are", first, second, third)

# arr = [34, 56, 22, 12, 68, 53]
# arr_size = len(arr)

# printlargest(arr, arr_size)

#------------------------------------
# this method uses tuned quicksort with avg, case time complexity = O(nlogn)

# def find3largest(arr, n):
#     arr = sorted(arr)

#     check = 0
#     count = 1

#     for i in range(1, n+1):
#         if (count < 4):
#             if (check != arr[n-i]):

#                 # to handle duplicate values
#                 print(arr[n-i], end = " ")
#                 check = arr[n-i]
#                 count += 1
#             else:
#                 break

# arr = [12, 45, 1, -1, 45, 54, 23, 5, 0, -10]
# n= len(arr)
# find3largest(arr, n)


#------------------------------------
# we can use partial sort of c++ STL

V = [ 11, 65, 193, 36, 209, 664, 32 ]
V.sort()
V.reverse()

print(f"first = {V[0]}")
print(f"first = {V[1]}")
print(f"first = {V[2]}")