#-------------------- Iterative Method to delete an element from the linked list:
class Node:
	# constructor to initialize the node object
	def __init__(self, data):
		self.number = data
		self.next = None


def push(head, A):
	n = Node(A)
	n.number = A
	n.next = head
	head = n
	return head


def deleteN(head, position):
	temp = head
	prev = head
	for i in range(0, position):
		if i == 0 and position == 1:
			head = head.next

		else:
			if i == position-1 and temp is not None:
				prev.next = temp.next
			else:
				prev = temp

				# Position was greater than
				# number of nodes in the list
				if prev is None:
					break
				temp = temp.next
	return head


def printList(head):
	while(head):
		if head.next == None:
			print("[", head.number, "] ", "[", hex(id(head)), "]->", "nil")
		else:
			print("[", head.number, "] ", "[", hex(
				id(head)), "]->", hex(id(head.next)))
		head = head.next
	print("")
	print("")


head = Node(0)
head = push(head, 1)
head = push(head, 2)
head = push(head, 3)

printList(head)

# Delete any position from list
head = deleteN(head, 1)
printList(head)



#-------------------- Delete the first node in a linked list where data == key:
# A complete working Python3 program to
# demonstrate deletion in singly
# linked list with class

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Given a reference to the head of a list and a key,
	# delete the first occurrence of key in linked list
	def deleteNode(self, key):

		# Store head node
		temp = self.head

		# If head node itself holds the key to be deleted
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		# Search for the key to be deleted, keep track of the
		# previous node as we need to change 'prev.next'
		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		# if key was not present in linked list
		if(temp == None):
			return

		# Unlink the node from linked list
		prev.next = temp.next

		temp = None

	# Utility function to print the linked LinkedList

	def printList(self):
		temp = self.head
		while(temp):
			print(" %d" % (temp.data)),
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()



#----------------------- Recursive Method to delete a node from linked list:
# Python program to delete a node in
# singly linked list recursively

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

# Deletes the node containing 'data'
# part as val and alter the head of
# the linked list (recursive method)
def deleteNode(head, val):
	# Check if list is empty or we
	# reach at the end of the
	# list.
	if (head == None):
		print("Element not present in the list")
		return -1
	# If current node is the
	# node to be deleted
	if (head.data == val):
		# If it's start of the node head
		# node points to second node
		if head.next:
			head.data = head.next.data
			head.next = head.next.next
			return 1
		else: return 0
	if deleteNode(head.next, val) == 0:
		head.next = None
		return 1

# Utility function to add a
# node in the linked list
# Here we are passing head by
# reference thus no need to
# return it to the main function
def push(head, data):
	newNode = Node(data)
	newNode.next = head
	head = newNode
	return head

# Utility function to print
# the linked list (recursive
# method)
def printLL(head):
	if (head == None):
		return
	temp = head
	while temp:
		print(temp.data,end=' ')
		temp = temp.next
	print()

# Driver Code

# Starting with an empty linked list
head = None
# Adds new element at the
# beginning of the list
head = push(head, 10)
head = push(head, 12)
head = push(head, 14)
head = push(head, 15)
# original list
printLL(head)
# Call to delete function
deleteNode(head, 20)
# 20 is not present thus no change
# in the list
printLL(head)
deleteNode(head, 10)
printLL(head)
deleteNode(head, 14)
printLL(head)
