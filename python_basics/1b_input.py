                            # TAKING MULTIPLE INPUT FROM USER USING SPLIT FUNCTION
                    
# a,b = input().split()      # No argument in split means that it will use a space to differentiate between values
# print("the values are {} and {}".format(a,b))
# print("the values are {1} and {0}".format(a,b))         #these values can be passed as index number starting from 0
# stri = "the values are {} and{}"                      #this is also a method to use format in python
# print(stri.format(a,b))
# print("Every {3} should know the use of {2} {1} programming and {0}"
    #   .format("programmer", "Open", "Source", "Operating Systems"))       #another method to use format method in python

                            # Python program showing how to take multiple input using split

# taking two inputs at a time
# x, y = input("Enter two values: ").split(',')
# print("Number of boys: ", x)
# print("Number of girls: ", y)
# print()

# taking three inputs at a time
# x, y, z = input("Enter three values: ").split('-')
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)
# print()

# taking two inputs at a time
# a, b = input("Enter two values: ").split()
# print("First number is {} and second number is {}".format(a, b))
# print()

# taking multiple inputs at a time and type casting using list() function
# x = list(map(int, input("Enter multiple values: ").split()))
# print("List of students: ", x)