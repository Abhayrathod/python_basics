#---------------approach 1 ( using hashing)
# Time Complexity: O(N)
# Auxiliary Space: O(N)

# def findmissingnumbrer(arr):

#     #find length of array
#     n = len(arr)

#     # create a list of zeroes
#     temp = [0] * (n+1)
#     print(temp)
#     for i in range(0, n):
#         temp[arr[i]-1] = 1
#     print(temp)
#     for i in range(0, n+1):
#         if(temp[i]==0):
#             ans = i+1

#     print(ans)


# if __name__ == "__main__":
#     arr = [1,2,3,5]

#     findmissingnumbrer(arr)

# #---------------approach 2 (Using summation of first N natural numbers)
# Time Complexity: O(N)
# Auxiliary Space: O(1)

# def getMissingNo(arr):
#     n = len(arr)
#     total = (n+1) * (n+2)/2
#     print(total)
#     sum_of_a = sum(arr)
#     print(sum_of_a)
#     return total - sum_of_a


# if __name__ == "__main__":
#     arr = [1,2,3,4]
#     print(getMissingNo(arr))


# #---------------approach 2 
# Modification for Overflow: The approach remains the same but there can be an overflow if N is large. 

# same method as above to avoid overflow if N is large
# Time Complexity: O(N) Only one traversal of the array is needed
# Auxiliary Space: O(1)

# def getMissingNo(arr):

#     N = len(arr)
#     i, total = 0,1

#     for i in range(2, N+2):
#         total += i
#         total -= arr[i-2]
#     return total
    
# if __name__ == "__main__":
#     arr = [1,2,3,5]

#     print(getMissingNo(arr))


# #---------------approach 3 (using binary operations)
# same method as above to avoid overflow if N is large
# Time Complexity: O(N) 
# Auxiliary Space: O(1)

# Python3 program to find
# the missing Number
# getMissingNo takes list as argument


def getMissingNo(a, n):
	x1 = a[0]
	x2 = 1

	for i in range(1, n):
		x1 = x1 ^ a[i]

	for i in range(2, n + 2):
		x2 = x2 ^ i

	return x1 ^ x2


# Driver program to test above function
if __name__ == '__main__':

	arr = [1, 2, 3, 5]
	N = len(arr)

	# Driver code
	miss = getMissingNo(arr, N)
	print(miss)



# -----------------Approach 4 (Using Cyclic Sort):
# Time Complexity: O(N), requires (N-1) comparisons
# Auxiliary Complexity: O(1)

# Python3 program to check missingNo

# def getMissingNo(arr, n) :
# 	i = 0
	
# 	while (i < n) :
# 		# as array is of 1 based indexing so the
# 		# correct position or index number of each
# 		# element is element-1 i.e. 1 will be at 0th
# 		# index similarly 2 correct index will 1 so
# 		# on...
# 		correctpos = arr[i] - 1
# 		if (arr[i] < n and arr[i] != arr[correctpos]) :
# 			# if array element should be lesser than
# 			# size and array element should not be at
# 			# its correct position then only swap with
# 			# its correct position or index value
# 			arr[i],arr[correctpos] = arr[correctpos], arr[i]

# 		else :
# 			# if element is at its correct position
# 			# just increment i and check for remaining
# 			# array elements
# 			i += 1
			
# 	# check for missing element by comparing elements with their index values
# 	for index in range(n) :
# 		if (arr[index] != index + 1) :
# 			return index + 1
			
# 	return n

# # Driver code
# if __name__ == "__main__" :
# 	arr = [ 1, 2, 3, 5 ]
# 	N = len(arr)
# 	print(getMissingNo(arr, N))
	
# -----------------------------Approach 5 (Use elements as Index and mark the visited places as negative):

# Time Complexity: O(N) 
# Auxiliary Space: O(1) 


# def findMissing(a, size):

# 	for i in range(0, n):
# 		if (abs(arr[i]) - 1 == size):
# 			continue

# 		ind = abs(arr[i]) - 1
# 		arr[ind] *= -1

# 	ans = size + 1
# 	for i in range(0, n):
# 		if (arr[i] > 0):
# 			ans = i + 1

# 	print(ans)

# # Driver Code
# if __name__ == '__main__':
# 	arr = [1, 3, 7, 5, 6, 2]
# 	n = len(arr)

# 	# Function call
# 	findMissing(arr, n)