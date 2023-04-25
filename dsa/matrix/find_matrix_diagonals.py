def print_matrix(arr):
    for i in range(4):
        for j in range(4):
            print(a[i][j], end=" ")
        print("")

def pricipal_diagonal(arr):
    print("principal diagonal: ",end="")

    for i in range(4):
        for j in range(4):
            if (i == j):
                print(arr[i][j], end=", ")
    
    print("")

def secondary_diagonal(arr):
    print("Secondary diagonal is: ",end="")

    for i in range(4):
        for j in range(4):
            if ((i + j) == (4-1)):
                print(arr[i][j], end=", ")

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print_matrix(a)
pricipal_diagonal(a)
secondary_diagonal(a)