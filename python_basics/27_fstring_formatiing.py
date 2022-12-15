import math
me = "abhay"
a1 = 3 
a = "this is %s %s"%(me,a1)
print(a)
b = "this is me {} {}"
b = "this is me {1} {0}"
c = b.format(me,a1)
print(c)

x = f"this is me {me} {a1} {4*34}"
x = f"this is me {me} {a1} {math.cos(65)}"
print(x)