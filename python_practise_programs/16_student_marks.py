print("Enter the marks of the students")
a,b,c,d,e = int(input()),int(input()),int(input()),int(input()),int(input())
if a>33 and b>33 and c>33 and d>33 and e>33:
    print("Result: Pass")
    per = (a+b+c+d+e)/5
    if per >= 60:
        print("First Division")
    elif per >= 50:
        print("Second Division")
    else:
        print("Third Divison")
else:
    print("Result : Fail")