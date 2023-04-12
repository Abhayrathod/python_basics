# ----------------Iterative approach to binary search
# It returns the location of given array
# If presents, else returns -1

# def binarySearch(arr, to_find):

#     arr.sort()
#     low = 0
#     high = len(arr)-1

#     while low<=high:
#         mid = low + (high-low) // 2

#         #check if target is present at mid
#         if arr[mid] == to_find:
#             return mid

#         #if target is greater, ignore left half
#         elif arr[mid] < to_find:
#             low = mid + 1
        
#         # if target is  smaller, ignore right half
#         else:
#             high = mid - 1

#     # if element is not present, return -1
#     return -1


# arr = [2,6,1,3,90,56,45,76]
# to_find = 56

# result = binarySearch(arr, to_find)

# if result != -1:
#     print("Element is present at index ", result)
# else:
#     print("Element is not present")


# -------------------------Another Iterative method

def binarySearch(v, To_Find):
	lo = 0
	hi = len(v) - 1

	# This below check covers all cases , so need to check
	# for mid=lo-(hi-lo)/2
	while hi - lo > 1:
		print("!!!!!!",hi-lo)
		mid = (hi + lo) // 2
		if v[mid] < To_Find:
			lo = mid + 1
		else:
			hi = mid

	if v[lo] == To_Find:
		print("Found At Index", lo)
	elif v[hi] == To_Find:
		print("Found At Index", hi)
	else:
		print("Not Found")


if __name__ == '__main__':
	v = [1, 3, 4, 5, 6]

	To_Find = 3
	binarySearch(v, To_Find)

	# To_Find = 6
	# binarySearch(v, To_Find)

	# To_Find = 10
	# binarySearch(v, To_Find)


# ---------------------------- Recursive approach

# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1


# def binarySearch(arr, l, r, x):

# 	# Check base case
# 	if r >= l:

# 		mid = l + (r - l) // 2

# 		# If element is present at the middle itself
# 		if arr[mid] == x:
# 			return mid

# 		# If element is smaller than mid, then it
# 		# can only be present in left subarray
# 		elif arr[mid] > x:
# 			return binarySearch(arr, l, mid-1, x)

# 		# Else the element can only be present
# 		# in right subarray
# 		else:
# 			return binarySearch(arr, mid + 1, r, x)

# 	else:
# 		# Element is not present in the array
# 		return -1


# # Driver Code
# arr = [2, 3, 4, 10, 40]
# x = 10

# # Function call
# result = binarySearch(arr, 0, len(arr)-1, x)

# if result != -1:
# 	print("Element is present at index % d" % result)
# else:
# 	print("Element is not present in array")
