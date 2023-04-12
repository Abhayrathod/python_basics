#-------------------------------------Method 1

# def sentinel_search(arr, n, key):
#     last = arr[n-1]
#     arr[n-1] = key

#     i=0
#     while arr[i] != key:
#         i+=1
    
#     arr[n-1] = last

#     if ((i<n-1) or (arr[n-1] == key)):
#         print(key, "is present at index", i)
#     else:
#         print("Element is not found")

# array = [10,20,180,45,67,70]
# n = len(array)
# key = 180

# sentinel_search(array, n, key)



#-------------------------------------Method 2

def sentinelLinearSearch(array, key):
	last = array[len(array) - 1]
	array[len(array) - 1] = key
	i = 0
	while array[i] != key:
		i += 1
	array[len(array) - 1] = last
	if i < len(array) - 1 or last == key:
		return i
	else:
		return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = 5
index = sentinelLinearSearch(array, key)
if index == -1:
	print(f"{key} is not found in the array: {array}")
else:
	print(f"{key} is found at index {index} in the array: {array}")
