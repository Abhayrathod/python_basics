# Python program for left rotation of matrix by 180
R = 4
C = 4

# Function to rotate the matrix by 180 degree
def reverseColumns(arr):
    for i in range(C):
        for j in range(0, int(C / 2)):
            x = arr[j][i]
            arr[j][i] = arr[C - 1 - j][i]
            arr[C - 1 - j][i] = x

# Function for transpose of matrix
def transpose(arr):
    for i in range(R):
        for j in range(i, C):
            x = arr[j][i]
            arr[j][i] = arr[i][j]
            arr[i][j] = x

# Function for display the matrix
def printMatrix(arr):
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end = ' ')
        print()

# Function to anticlockwise rotate matrix
# by 180 degree
def rotate180(arr):
    transpose(arr)
    reverseColumns(arr)
    transpose(arr)
    reverseColumns(arr)

# Driven code
arr = [[1, 2, 3, 4 ],
			[ 5, 6, 7, 8 ],
			[ 9, 10, 11, 12 ],
			[ 13, 14, 15, 16 ]]
rotate180(arr)
printMatrix(arr)

# This code is contributed by akashish__
