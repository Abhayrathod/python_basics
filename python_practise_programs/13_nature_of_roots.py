print("Enter the values of a,b,c")
a,b,c = int(input("Enter the value of a")),int(input("Enter the value of b")),int(input("Enter the value of c"))
d = b**2-4*a*c
if d>0:
    print("the nature of roots are real and distinct")
elif d == 0:
    print("The nature of roots are real and equal")
else:
    print("The nature of roots are imaginary")