#------------dictionary is ordered and changeable

# a = {'key':'value', 'cow':'mooh'}
# print(a['cow'])
#will print "mooh" on the screen
# Dictionary is nothing but key value pairs
# d1 = {}
# print(type(d1))
# d2 = {"Harry":"Burger",
#       "Rohan":"Fish",
#       "SkillF":"Roti",
#       "Shubham":{"B":"maggie", "Leena":"roti", "D":"Chicken"},
#       "angur":"Fish"}
# d2["Ankit"] = "Junk Food"
# d2[420] = "Kebabs"
# del d2[420]
# print(d2)
# print(d2["Shubham"])
# d3 = d2.copy()
# del d3["Harry"]
# print(d3)
# d2.update({"Leena":"Toffee"})
# d2.update({"Leena":"chai"})
# print(d2)
# print(d2.keys())
# print(d2.values())
# print(d2)
# print(d2.items())


#-------------------–––---–––––––dict comprehesion---------------------------
dict1 = {i:f"item {i}" for i in range(1,1101) if i%100==0}
print(dict1)

dict2 = {value:key for key,value in dict1.items()}
print(dict2)