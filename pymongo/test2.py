from re import L
import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Betfair"]
mycol = mydb["betfair"]

mycol.create_index( [("updt", -1)] )
# myquery = {"updt": {"$lt":1661413597000}}


# mydoc = mycol.find_one(myquery,sort=[( 'updt', pymongo.DESCENDING,)])
# mydoc2 = mycol.find_one(myquery,sort=[( 'updt', pymongo.ASCENDING,)])
# i = 1
# for x in mydoc:
#     t = datetime.datetime.fromtimestamp(x["updt"]/1000,tz=None)
#     print(f"{i}   {t}")
#     i +=1
#     break
# t = mydoc["updt"]
# t2 = mydoc2["updt"]
# print(mydoc)
# print(t > t2)


# print(datetime.datetime.fromtimestamp(1651436848000/1000, tz =None))
# print(datetime.datetime.fromtimestamp(1651435866000/1000, tz =None))


# myquery = {"eventId" : 32986793,"marketId" :1 ,"signId" :3, "updt" :{"$lt":1660015863000}}
# mydoc = mycol.find_one(myquery)
# print(mydoc)
# for x in mydoc:

#     print(x["updt"])



# t = datetime.datetime.now().timestamp() - (30 * 60000)
# print(t)

mydict = {
    "eventId" : 32986793,
    "bookmakerId" : 2,
    "marketId" : 1,
    "signId" : 3,
    "sbv" : "#",
    "backOdd" : 5,
    "updt" : 1659967350
}
x = mycol.insert_one(mydict)

# myquery = {"eventId" : 32986793,"marketId" :1 ,"signId" :3, "updt" :{"$lt":1660015863000}}
# from  script import getResult
# import time
# start = time.process_time()
# mydoc = mycol.find().distinct('eventId')
# mydoc2 = mycol.find().distinct('marketId')
# mydoc3 = mycol.find().distinct('signId')

# eventID = [x for x in mydoc]
# marketID = [x for x in mydoc2]
# signID = [x for x in mydoc3]
# qtime = int(datetime.datetime.now().timestamp()) -(time * 60000)
# qtime2 = int(datetime.datetime.now().timestamp())-((time + 15) * 60000)
# myquery = [{"updt": {"$gt":qtime2,'$lt':qtime}}, {"$group": {"_id": {"event": "$eventId", "market": "$marketId", "sign": "$signId"}}}]
# mydoc = mycol.aggregate(myquery)
# l = []
# for x in mydoc:
#     l.append(x)
# print(len(l))
# # print(len(eventID))

# for x in l:
#     eventId = x['_id']["event"]
#     marketId = x['_id']["market"]
#     signId = x['_id']["sign"]
#     getResult(eventId,marketId,signId)

# print(time.process_time() - start)
# myscript = {"eventId": l[0]}
# mydoc2 = mycol.find(myscript)

# for x in mydoc2:
#     print(x)
# l = []
# mydoc = mycol.find().distinct('_id')
# for x in mydoc:
#   l.append(x)
# print(l[-1])


# mydoc = mycol.find()
# for x in mydoc:
#     print(x)