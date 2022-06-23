from numpy import *

# where() - This function is used to create a new array which contains, returned element chosen from \
#  expression1 or expression2 depending upon the condition. If condition is True expresssion1 is executed \
    #  else expression 2

    # syntax - numpy.where(condition, expression1, expression2)

a = array([100,200,300,400,500])
b = array([100,200,3,4,500])

c = where(b>a,a,b)
print(c)
