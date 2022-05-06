from pip import main


def printstr(str):
    return(f"this is an example string {str}")

def add(num1,num2):
    return num1 + num2

print("the name is",__name__)
if __name__=='__main__':
    print(printstr("new string"))
    u = add(4,5)
    print(u)