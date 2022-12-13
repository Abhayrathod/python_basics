# %- modulo operator, interpolation operator
# syntax - print("format placeholder"%(data))
# format placeholder = %[flags][width][.precision]type
# data - It can be literal, variable , expresssion etc


# print("%d"% 432)
# print("%d %d"% (432, 345))      # value ek se jyada ho tab paranthesis me likhna padta hai
# print("%d %f"% (432, 345))
# print("%f"% 432.123)
# print("%f"% 432.123456789)          #only shows value up to six digits by rounding the sixth digit
# print("%f %f"% (432, 3.0))          # shows five value after decimal even when you input only one digit after decimal
# print("%s"% "abhay")
# print("%s %s"% ("abhay","abhay2"))
# print("%s %d"%("abhay",45))
# print("%s %d"%(45,"abhay"))             # this will generate ERROR because sequence is not right

#----- we have to use key value pair like that in dictionary in order to avoid sequence error
# print("%d %f"%(45.0,45))            # this however did not generate error and i dont know why maybe both are integers
# print("%(name)s %(ag)d "%{"ag":45, "name":"abhay"})

#------also we can write like this
# a = "%s" %45
# print(a)

#--------flags
# print("%d" %45)
# print("% d" %45)
# print("%       d" %45)          # only one space is allowed no matter how many you give
# print("%+d" %45)

# #------width
# print("%8d" %45345)             # this shows width and 8 will create 8 boxes in which input values will be filled from 
#                                 # left to right  , if values provided are less it will show space

# #---- using flag with width
# print("%+12d"%453)      
# print("%+56d"%28352389723834)      # this will not print + in empty spaces dont know why
# print("%-56d"%28352389723834)      # this will not print - in empty spaces dont know why
# print("%056d"%28352389723834)       # this will print 0 in rest of the empty spaces 


#------using precision
print("%f"% 432.123355)
print("%.3f"% 432.123355)              # this will give precision of only three after decimal because we have mentioned it
print("%.4s"%"dsfsnfjknds")             #precision also works on string TRY  DIFFERENT COMBINATIONS LIKE THIS
print("%.2f"%3545.326)                  # this will round the digit up to two decimal
print("%09.3f"%25378.2357235328)         # ye sirf decimal k baad ka hi consider karta hai isliye width kaam anhi karegi yaha
                                        #kyuki shyad kisiko crore ka nuksan ho jaye isliye , sochna esa kyu
print("%09.3d"%25378.2357235328)

#----also
print("this is %d rs" % 45)
a = "this is %d rs" % 45
print(a)
