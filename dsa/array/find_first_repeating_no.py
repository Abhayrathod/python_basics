# -------------------------Approach 1
# Find the first repeating element in an array of integers using Hashset



# def printFirstRepeating(arr, n):

# 	# Initialize index of first repeating element
# 	Min = -1

# 	# Creates an empty hashset
# 	myset = dict()

# 	# Traverse the input array from right to left
# 	for i in range(n - 1, -1, -1):

# 		# If element is already in hash set,
# 		# update Min
# 		if arr[i] in myset.keys():
# 			Min = i

# 		else: # Else add element to hash set
# 			myset[arr[i]] = 1

# 	# Print the result
# 	if (Min != -1):
# 		print("The first repeating element is",
# 			arr[Min])
# 	else:
# 		print("There are no repeating elements")


# # Driver Code
# arr = [10, 5, 3, 4, 3, 5, 6]

# n = len(arr)
# printFirstRepeating(arr, n)


#--------------------------Approach 2
# Find the first repeating element in an array of integers using Hashing 


def printFirstRepeating(arr, n):
 
    # This will set k=1, if any
    # repeating element found
    k = 0
 
    # max = maximum from (all elements & n)
    max = n
 
    for i in range(n):
        if (max < arr[i]):
            max = arr[i]
 
    # Array a is for storing
    # 1st time occurrence of element
    # initialized by 0
    a = [0 for i in range(max + 1)]
 
    # Store 1 in array b
    # if element is duplicate
    # initialized by 0
    b = [0 for i in range(max + 1)]
 
    for i in range(n):
 
        # Duplicate element found
        if (a[arr[i]]):
            b[arr[i]] = 1
            k = 1
            continue
        else:
 
            # Storing 1st occurrence of arr[i]
            a[arr[i]] = i+1
 
    if (k == 0):
        print("No repeating element found")
    else:
        min = max + 1
 
        for i in range(max + 1):
 
            # Trace array a & find repeating
            # element with min index
            if (a[i] and (min > (a[i])) and b[i]):
                min = a[i]
 
        print(arr[min-1])
 
 
# Driver code
arr = [10, 5, 3, 4, 3, 5, 6]
N = len(arr)
 
printFirstRepeating(arr, N)