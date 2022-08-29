# a = 'geeks for geeks'
# print(set(a.split(' ',2)))



#----------------list comprehension-------------
# lst = []
# for i in range(100):
#     if i%3 ==0:
#         lst.append(i)
# print(lst)

# lst = [i for i in range(100) if i%3==0] #this is list comprehension in python
# print(lst)

# lst= [int(input("Enter the numbers").split(','))]
# for i in lst:
#     if i%2 ==0:
#         print(str(i),"the number is even")
#     else:
#         print(str(i),"the number is odd"). /


# iter_list = iter([input("Enter the characters").split('-')])
# iter_list = iter([input("Enter the characters").split('-')])
# print((next(iter_list)))
# print((next(iter_list)))


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

#-------------------method 1-------
# ans = [[i,j,k] for i in range(0,x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
# print(ans)
#-------------------method 2-------
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 print([i,j,k],end='')


# n1 = [1,2,3]
# n2 = [4,5,6]
# result = map(lambda x,y:x+y,n1,n2)

#---------------------------------------------------


# def func(fun):

#     def inn_fa():
#         print("this is before the func execution")
#         fun()
#         print("this is after func execution")
#     return inn_fa

# def p_func():
#     print("this is inside func")
# var = func(p_func)
# var()


#-------------------------------------------test task

# import pymongo
# import datetime

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["Betfair"]
# mycol = mydb["betfair"]

# # for i in mycol.find():
# #     return_obj = {}
# #     return_obj["updt"] = datetime.fromtimestamp(i.get("updt")).strftime('%Y-%m-%d %H:%M:%S.%f%z (%Z)') 
# #     print("---return_obj----", return_obj)
# # for i in mycol.find().sort("updat", -1)
# ex_last = mycol.
# 



# find().sort("backOdd", -1).limit(1)
# for i in ex_last:
#     print(i)
#     odds_last = i['backOdd']
#     odds_time = i["updt"]
# odd = odds_last
# for i in ex_desc:
#     odds_time = i["updt"]
#     odds_back = i['backOdd']
# def increment()i = 15
# while True:
#     i+=15
#     if i==300:
#         break

# odds_last = odd - datetime.timedelta(minutes = 15)
# print(odds_last)


# for i in ex:
#     odds_last = i['updt']

    # return_obj["id"] = i.get("eventId")
    # return_obj["marketId"] = i.get("marketId")
    # return_obj["signId"] = i.get("signId")
    # return_obj["odd"] = i.get("backOdd")
    # return_obj["updt"] = i.get("updt")



#----------------------------------task working

import pymongo
import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Betfair"]
mycol = mydb["betfair"]
time = mycol.find_one(sort=[( '_id', pymongo.DESCENDING )])["updt"]
# print(time)
time2 = datetime.datetime.fromtimestamp(int(time)/1000)
# print(time2)
return_obj = {}
# ex = mycol.find().sort("updt", -1).limit(1)
# for i in ex:
#     before15 = datetime.datetime.now() - datetime.timedelta(minutes = 15)
myquery = { "updt": time - 900000 }
mydoc = mycol.find_one(myquery,sort=[( 'eventId', pymongo.DESCENDING )])
# for x in mydoc:
#   print(x)
# print(mydoc)
def getvalue(timetoget):
    myquery = { "updt": time - int(timetoget) * 60000 }
    mydoc = mycol.find_one(myquery,sort=[( 'eventId', pymongo.DESCENDING )])
    if mydoc:
     return mydoc["backOdd"]
    else:
        return None
return_obj["odd-15"] = getvalue(15)
return_obj["odd-30"] = getvalue(30)
return_obj["odd-45"] = getvalue(45)
return_obj["odd-60"] = getvalue(60)
return_obj["odd-75"] = getvalue(75)
return_obj["odd-90"] = getvalue(90)
return_obj["odd-105"] = getvalue(105)
return_obj["odd-120"] = getvalue(120)
return_obj["odd-135"] = getvalue(135)
return_obj["odd-150"] = getvalue(150)
return_obj["odd-165"] = getvalue(165)
return_obj["odd-180"] = getvalue(180)
return_obj["odd-195"] = getvalue(195)
return_obj["odd-210"] = getvalue(210)
return_obj["odd-225"] = getvalue(225)
return_obj["odd-240"] = getvalue(240)
return_obj["odd-255"] = getvalue(255)
return_obj["odd-270"] = getvalue(270)
return_obj["odd-285"] = getvalue(285)
return_obj["odd-300"] = getvalue(300)
print(return_obj)