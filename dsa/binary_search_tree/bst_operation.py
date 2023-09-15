# Python program to insert a node
# in a BST

# Given Node
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to insert a new node with
# given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)

# Driver Code
if __name__ == '__main__':
	"""
	Let us create following BST
		50
	/	 \
	30	 70
	/ \ / \
	20 40 60 80
	"""
	root = None

	# Inserting value 50
	root = insert(root, 50)

	# Inserting value 30
	insert(root, 30)

	# Inserting value 20
	insert(root, 20)

	# Inserting value 40
	insert(root, 40)

	# Inserting value 70
	insert(root, 70)

	# Inserting value 60
	insert(root, 60)

	# Inserting value 80
	insert(root, 80)

	# Print the BST
	inorder(root)
	
#This code is contributed by japmeet01

#------------------------------------

# Python program to implement
# inorder traversal of BST

# Given Node node
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to create a new BST node
def newNode(item):
	temp = Node(item)
	temp.key = item
	temp.left = temp.right = None
	return temp

# Function to insert a new node with
# given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return newNode(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Function to do inorder traversal of BST
def inorder(root):
	if root:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)

# Driver Code
if __name__ == '__main__':
	
	# Let us create following BST
	#		 50
	#	 /	 \
	#	 30	 70
	# / \ / \
	# 20 40 60 80
	root = None

	# Creating the BST
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function Call
	inorder(root)
#This code is contributed by japmeet01

#------------------------------------

# Python program to implement preorder traversal
class Node:
	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to insert a new node with
# given key in BST


def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Function to do preorder traversal of BST


def preOrder(root):
	if root:
		print(root.key, end=" ")
		preOrder(root.left)
		preOrder(root.right)


# Driver Code
if __name__ == '__main__':
	"""
		Let us create following BST
			50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80
"""
	root = None
	keys = [50, 30, 20, 40, 70, 60, 80]

	# Creating the BST
	for key in keys:
		root = insert(root, key)

	# Function Call
	preOrder(root)
#This code is contributed by japmeet01

#---------------------------------------------

# Python program to print total count of nodes in BST

# Define the Node class
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to insert a new node with given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Function to do postorder traversal of BST
def postOrder(root):
	if root:
		postOrder(root.left)
		postOrder(root.right)
		print(root.key, end=" ")

# Driver code
if __name__ == '__main__':
	# Let us create following BST
	#		 50
	#	 /	 \
	#	 30	 70
	#	 / \ / \
	# 20 40 60 80

	root = None

	# Creating the BST
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function call
	postOrder(root)

	#This code is contributed by japmeet01

#-------------------------------------------

# Python program to implement
# level order traversal
import queue

# Given Node node
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to insert a new node with
# given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Returns height of the BST
def height(node):
	if node is None:
		return 0
	else:
		# Compute the depth of each subtree
		lDepth = height(node.left)
		rDepth = height(node.right)

		# Use the larger one
		if lDepth > rDepth:
			return (lDepth + 1)
		else:
			return (rDepth + 1)

# Print nodes at a given level
def printGivenLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root.key, end=" ")
	elif level > 1:
		# Recursive call
		printGivenLevel(root.left, level - 1)
		printGivenLevel(root.right, level - 1)

# Function to line by line print
# level order traversal of a tree
def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printGivenLevel(root, i)
		print()

# Driver Code
if __name__ == '__main__':
	# Let us create following BST
	#		 50
	#	 /	 \
	#	 30	 70
	#	 / \ / \
	# 20 40 60 80
	root = None

	# Creating the BST
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function Call
	printLevelOrder(root)
	
	#This code is contributed by japmeet01

#------------------------------------------

# Python program to print nodes at a given level

# Given Node node


class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to insert a new node with
# given key in BST


def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Print nodes at a given level


def printGivenLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root.key, end=' ')
	elif level > 1:
		# Recursive Call
		printGivenLevel(root.left, level - 1)
		printGivenLevel(root.right, level - 1)


# Driver Code
if __name__ == '__main__':
	# Let us create following BST
	#		 50
	#	 /	 \
	#	 30	 70
	#	 / \ / \
	#	 20 40 60 80
	root = None

	# Creating the BST
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function Call
	printGivenLevel(root, 2)

	# This code is contributed by japmeet01

#--------------------------------------------

# Python program to print all
# leaf nodes of a BST

# Given Node node
class Node:
	def __init__(self, item):
		self.key = item
		self.left = None
		self.right = None

# Function to insert a new node with
# given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Function to print leaf nodes
# from left to right
def printLeafNodes(root):
	# If node is null, return
	if not root:
		return

	# If node is leaf node,
	# print its data
	if not root.left and not root.right:
		print(root.key, end=" ")

	# If left child exists,
	# check for leaf recursively
	if root.left:
		printLeafNodes(root.left)

	# If right child exists,
	# check for leaf recursively
	if root.right:
		printLeafNodes(root.right)

# Driver Code
if __name__ == "__main__":
	# Let us create following BST
	#		 50
	#	 / \
	#	 30	 70
	#	 / \ / \
	# 20 40 60 80

	# Creating the BST
	root = None
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function Call
	printLeafNodes(root)

	#This code is contributed by japmeet01

#--------------------------------------------

# Python program to print all
# non leaf nodes of a BST

# Given Node node


class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to insert a new node with
# given key in BST


def insert(root, key):
	# If the tree is empty, return a new node
	if root is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < root.key:
		root.left = insert(root.left, key)
	elif key > root.key:
		root.right = insert(root.right, key)

	# Return the node pointer
	return root

# Function to print all non-leaf
# nodes in a tree


def printNonLeafNode(root):
	# Base Cases
	if root is None or (root.left is None and root.right is None):
		return

	# If current node is non-leaf,
	if root.left is not None or root.right is not None:
		print(root.key, end=" ")

	# If root is Not NULL and its one
	# of its child is also not NULL
	printNonLeafNode(root.left)
	printNonLeafNode(root.right)


# Driver Code
if __name__ == '__main__':
	# Let us create following BST
	#		 50
	#	 /	 \
	#	 30	 70
	#	 / \	 / \
	# 20 40 60 80

	root = None

	# Creating the BST
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function Call
	printNonLeafNode(root)

	# This code is contributed by japmeet01

#--------------------------------------

# Python program to print right view of a BST
import sys

# Given Node node
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to insert a new node with
# given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Function to print the right view
# of a binary tree.
def rightViewUtil(root, level, max_level):
	# Base Case
	if root is None:
		return

	# If this is the last Node of its level
	if (max_level[0] < level):
		print("\t", root.key, end="")
		max_level[0] = level

	# Recur for right subtree first,
	# then left subtree
	rightViewUtil(root.right, level + 1, max_level)
	rightViewUtil(root.left, level + 1, max_level)

# Wrapper over rightViewUtil()
def rightView(root):
	max_level = [0]
	rightViewUtil(root, 1, max_level)

# Driver Code
if __name__ == "__main__":
	# Let us create following BST
	#	 50
	#	 /	 \
	# 30	 70
	# / \ / \
	# 20 40 60 80

	root = None

	# Creating the BST
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function Call
	rightView(root)
	
	#This code is contributed by japmeet01

#-------------------------------------------

# Python program to print
# left view of a BST

# Given Node node


class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to insert a new node with
# given key in BST


def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Function to print left view of
# binary tree


def leftViewUtil(root, level, max_level):
	# Base Case
	if root is None:
		return

	# If this is the first node
	# of its level
	if max_level[0] < level:
		print(root.key, end=" ")
		max_level[0] = level

	# Recur for left and right subtrees
	leftViewUtil(root.left, level + 1, max_level)
	leftViewUtil(root.right, level + 1, max_level)

# Wrapper over leftViewUtil()


def leftView(root):
	max_level = [0]
	leftViewUtil(root, 1, max_level)


# Driver Code
if __name__ == '__main__':
	# Let us create following BST
	#		 50
	#	 / \
	#	 30	 70
	#	 / \ / \
	# 20 40 60 80
	root = None

	# Creating the BST
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function Call
	leftView(root)
	
	#This code is contributed by japmeet01

#-------------------------------------------------