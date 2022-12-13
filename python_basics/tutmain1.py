#-----------------HARRY LEARNINIG
# def printstr(str):
#     return(f"this is an example string {str}")

# def add(num1,num2):
#     return num1 + num2

# print("the name is",__name__)
# if __name__=='__main__':
#     print(printstr("new string"))
#     u = add(4,5)
#     print(u)


#---------------LEARNED FROM FREECODECAMP.ORG-----
from tutmain2 import function_three


print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == '__main__':
    print("File one executed when ran directly")
    function_two()
    function_three()
else:
    print("File one excuted when imported")