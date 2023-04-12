#----------------------------------Approach 1 
# Time complexity: O(N) 
# Auxiliary Space: O(N)


# def rotate(a, d, N):
#     k = a.index(d)
#     new_list = []
#     new_list = a[k+1:]+a[0:k+1]
#     return new_list



# if __name__ == "__main__":
#     arr = [1,2,3,4,5,6,7,8]
#     d =2
#     N = len(arr)

#     arr = rotate(arr,d, N)
#     for i in arr:
#         print(i, end=' ')


#----------------------------------Approach 2
# Time Complexity: O(N * d)
# Auxiliary Space: O(1)

# def rotateArray(arr, d, N):
#     p = 1
#     while(p<=d):
#         last = arr[0]
#         for i in range(N-1):
#             arr[i] = arr[i+1]
#         arr[N-1] = last
#         print(arr)
#         p += 1
    
# def printArray(arr, N):
#     for i in range(N):
#         print(arr[i], end=' ')

# arr = [1,2,3,4,5,6,7,8]
# N = len(arr)
# d = 2
# rotateArray(arr, 2, N)
# printArray(arr, N)


#----------------------------------Approach 3
# Time complexity : O(N) 
# Auxiliary Space : O(1)


def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    print(g_c_d)
    for i in range(g_c_d):
 
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
 
# UTILITY FUNCTIONS
# function to print an array
 
 
def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")
 
# Function to get gcd of a and b
 
 
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
 
 
# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
d = 2
leftRotate(arr, d, n)
printArray(arr, n)