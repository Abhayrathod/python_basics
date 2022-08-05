# dict1= {"Best Python Course": "CodeWithHarry",
#         "Best C Languge Course": "CodeWithHarry",
#         "Harry Sir":"Tom Cruise Of Programming"
#         }

# for x,y in dict1.items():
#     print(x ,":", y)

list1 = [ ["Harry", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
# dict1 = dict(list1)
# print(dict1)
# for a in list1:
#     print(a)


#-------------------------------ek list mese do value ko nikal k , do alag list me add kiya hai
# items= []
# value= []
# for x,y in list1:
#     items.append(x),value.append(y)
# print(items,value)

#-----------------------list ki value ko nikal k dictionary me add kiya hai
dct = {}
for x in list1:
    for i in range(len(x)):
        a = x[i]
        
        

print(dct)


# for item,value in dict1.items():
#     print(item,value)

# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)

# items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

# for item in items:
#     if str(item).isnumeric() and item>=6:
#         print(item)