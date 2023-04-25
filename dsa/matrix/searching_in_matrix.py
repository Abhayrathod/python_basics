a = [[1,2,3],[4,5,6],[7,8,9]]
# a = [int(input("Enter the array for matrix: "))]

find = int(input("Enter the element you want to find: "))

def search_matrix(arr, find):

    for i in range(3):
        for j in range(3):
            return 1 if a[i][j] == find else 0

if search_matrix(a, 6):
    print("Number exists in array")
else:
    print("Number does not exist.")