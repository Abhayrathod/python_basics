print("Enter three numbers")
a,b,c = int(input()),int(input()),int(input())
if a>b:
    if a>c:
        print(f"The {a} is greater no")
elif b>c:
    print(f"{b} is greater no")
else:
    print(f"{c} is greater no")