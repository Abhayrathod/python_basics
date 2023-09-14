# Python3 program to construct binary
# tree from given array in level
# order fashion Tree Node

# Helper function that allocates a
#new node
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

# Function to insert nodes in level order
def insertLevelOrder(arr, i, n):
	root = None
	# Base case for recursion
	if i < n:
		root = newNode(arr[i])

		# insert left child
		root.left = insertLevelOrder(arr, 2 * i + 1, n)

		# insert right child
		root.right = insertLevelOrder(arr, 2 * i + 2, n)
		
	return root

# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
	if root != None:
		inOrder(root.left)
		print(root.data,end=" ")
		inOrder(root.right)

# Driver Code
if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
	n = len(arr)
	root = None
	root = insertLevelOrder(arr, 0, n)
	inOrder(root)
	
#----------------------approach 2 : using queue

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def buildTree(nums):
	if not nums:
		return None
	root = TreeNode(nums[0])
	q = [root]
	print("--------q-----------",q)
	i = 1
	while i < len(nums):
		curr = q.pop(0)
		print("----- q in loop---------",q)
		print(f"----- {i} curr---------",curr)
		if i < len(nums):
			curr.left = TreeNode(nums[i])
			q.append(curr.left)
			i += 1
		if i < len(nums):
			curr.right = TreeNode(nums[i])
			q.append(curr.right)
			i += 1
		print(f"----- {i} end---------",q)
	return root

def printTree(root):
	if not root:
		return
	printTree(root.left)
	print(root.val, end=" ")
	printTree(root.right)

nums = [1, 2, 3, 4, 5, 6, 6, 6, 6]
root = buildTree(nums)
printTree(root)
