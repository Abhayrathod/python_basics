c = complex(input("Enter the no : "))
if c.real>c.imag:
    print("%d is greater"%(c.real))
if c.real<c.imag:
    print("%d is greater"%(c.imag))
else:
    print("Both are equal")