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