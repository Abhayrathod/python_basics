#-------------------- Iterative approach to the problem

# def reverseListI(arr, start, end):
#     while start<end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#     return arr

# A = [1,2,3,4,5,6]
# reverse = reverseListI(A, 0, 5)
# print(reverse)


# #--------------------recursive approach

# def reverseListR(arr, start, end):
#     if start>=end:
#         return
#     A[start], A[end] = A[end], A[start]
#     reverseListR(arr, start+1, end-1)

# A = [1,2,3,4,5,6]
# reverseR = reverseListR(A, 0, 5)
# print(reverseR)             #printing this gives none, unlike iterative approach because , operations are performed on list itsef and not on "arr".
# print(A)


#----------------another approch - python list slicing

# def reverseList(arr):
#     print(arr[::-1])

# A = [1,2,3,4,5,6]
# reverseList(A)