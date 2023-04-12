# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

def search_list(arr, len, target):

    for position in range(0, len):
        if (arr[position]==target):
            return position
    return -1


if __name__ == "__main__":
    arr = [2,3,4,5,6,7,8]
    length = len(arr) - 1
    result = search_list(arr, length, 8)
    if result == -1:
        print("Element is not present in the array")
    else:
        print("Element is present at index: ",result)



# """Python Program to Implement Linear Search Recursively"""


def linear_search(arr, key, size):

# If the array is empty we will return -1
	if (size == 0):
		return -1

	elif (arr[size - 1] == key):
		# Return the index of found key.
		return size - 1
	else:
		return linear_search(arr, key, size - 1)


# Driver's code
if __name__ == "__main__":
	arr = [5, 15, 6, 9, 4]
	key = 4
	size = len(arr)
	ans = linear_search(arr, key, size) # Calling the Function
	if ans != -1:
		print("The element", key, "is found at",
			ans, "index of the given array.")
	else:
		print("The element", key, "is not found.")

# Code Contributed By - DwaipayanBandyopadhyay
# Code is modified by Susobhan Akhuli
