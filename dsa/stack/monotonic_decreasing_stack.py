# Python code to implement the approach

# Function to find a Monotonic
# decreasing stack
def decreasingStack(arr, N):
	stack = []
	for i in range(N):
	
		# Either stack empty or
		# all smaller nums are popped off
		while len(stack)>0 and stack[-1] < arr[i]:
			stack.pop()
		stack.append(arr[i])
		
	N2 = len(stack)
	ans = [0]*N2
	j = N2-1
	
	# Empty Stack
	while stack != []:
		ans[j] = stack.pop()
		j -= 1
	
	# Displaying the original array
	print('The array: ',end = ' ')
	for i in range(N):
		print(arr[i],end = ' ')
	print()
	
	# Displaying Monotonic Decreasing Stack
	print('The array: ',end = ' ')
	for i in range(N2):
		print(ans[i],end = ' ')
	print()
		
# Driver code
arr = [15, 17, 12, 13, 14, 10]
N = len(arr)

# Function call
decreasingStack(arr, N)

# This code is contributed by hardikkhuswaha.
