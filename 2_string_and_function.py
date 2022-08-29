# String Functions:

# demo = "Aakash is a proogrammer"
# print(demo)
# print(demo.endswith("boy"))
# print(demo.count('o'))
# print(demo.capitalize())
# print(demo.upper())
# print(demo.lower())
# print(demo.find("is"))     #returns the position of the starting character of the string you are searching (index starts from 0)
# print(demo.find("aakash","a"))
# print(demo[13])
# print(demo[2:6])
# print(demo[0:11:2])
# print(demo[:])
# print(demo[::])         #by default last vale colon k bad vaha pr one man leta hai
# print(demo[::2])  
# print(demo[-1:-12])   
# print(demo[::-3])   
# print(demo[-5:-3])
# print(demo.isalnum())      #space hatane se value true return karta hai
# print(demo.strip())
# print(demo.split(','))

#---------------strip function in string


# demo1 = "  this is string with left space and also little right  "
# demo2 = "  this is string with right space and also little on left    "
# demo3 = "       this is string with both left and right space     "
# print(demo1.lstrip())
# print(demo2.rstrip())
# print(demo3.strip())

# mystr = "Harry is a prooooogrammer"
# print(len(mystr))
# print(mystr[::-2])

# print(mystr.endswith("bdoy"))
# print(mystr.count("o"))
# print(mystr.capitalize())
# print(mystr.replace("is", "are"))


# age = '25'
# txt = "my name is abhay"+   age
# print(txt)

# quantity = '25'
# age = '16'
# price = '43'
# falana = 'falaaaana'
# dhekna = 'dheknaaaa'

# order = "i bought {} apples and my  age  is {} year {},{}"

# print(order.format(quantity, age,falana,dhekna))

#---------------------------------------------------lerning from geekyshows
# str1 = "geekyshows"
# for i in str1:
#     print(i)

# str2 = "hello this is 'me' and how are you?"
# str3 = 'hello this is "me" and how are you?'
# print(str2)
# print(str3)

# str4 = "demonstration"
# str5 = "demonstration"

# print(id(str4))
# print(id(str5))         # you will finfd that the id of both the varibale str4 and str5 is same because memory allocation is 
#                             # done on values and not on integer
                        
# str6 = "new day new opportunity"
# str6 = "with lot more excitement"
# print(id(str6))                     # here the latest value will be used and the previous value will be removbed from the 
                                    # memory because of the garbage collector in python

#----------escape sequences in string

# str7 = "this is a \ndemo string"
# print(str7)
# str8 = "this is a \tdemo string"
# print(str8)

# str9 = r"this type of string is \ncalled row string"               # row string basically ignore escape sequences and 
# print(str9)                                                        # prints the string as it is

#-------------try
# str10 = 'this'
# str10[2] = 't'              # not possible because string is immutable
# print(str10)

#-------------for loop in string
# str11 = "this is a demo string for 'for' loop"

# for i in str11:
#     print(i)
#     # print (len(str11))        # for fun try it and understand what happened

# for x in range(len(str11)):        # using for loop with index
#     print(str11[x])

#------------while loop in string
# str12 = "this is a demo for 'while' loop"

# i = 0
# while i<=len(str12):
#     print(str12[i])
#     i +=1

#-----------repetation operator
# print("$" * 10)
# str13 = "this"
# print(str13*10)
# print(str13[0:2]*8)

#----------concatenation operator
# def pr():
#     return "geeky" + "shows"
# a = "abhay"
# b = "singh"
# print(a+b+pr())
# print(a+b,pr())     # know the difference between this and above line

#-----------comparison operator
        # < less than
        # > greater than
        # <= less than or equal to
        # >= greate than or equal to
        # == Equal to
        # != Not equal to

# str14 = "A"
# str15 = "B"
# print(str14<str15)
# print(str14>str15)
# print(str14<=str15)
# print(str14>=str15)
# print(str14==str15)
# print(str14!=str15)
# print(0<1)
# print("acorn">"acoustic")



#---------------------------------------split function on time string
time_obj = "2022-05-23 14:10:58+00"
def sort_time(time:str):
    if time is None:
        return time 
    else:   
        time_lst = time.split()
        return time_lst[0] + " " + time_lst[1].strip("+00")


a = sort_time(time_obj)
print(a)