# import datetime

# print(datetime.datetime.now().timestamp() - (30*60000))



import pymongo
from bson.son import SON
import pprint
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Betfair"]
mycol = mydb["betfair"]

# mycol.create_index( [("updt", -1)] )
import datetime
# pipeline = [
#     {"$unwind": "$eventId"},
#     {"$group": {"_id": "$eventId", "count": {"$sum": 1}}},
#     {"$sort": SON([("count", -1), ("_id", -1)])}
# ]
# print(datetime.datetime.now().timestamp()-(30*60000))

# pprint.pprint(list(mydb.things.aggregate(pipeline)))
qtime = int(datetime.datetime.now().timestamp()) -(15 * 60000)
qtime2 = int(datetime.datetime.now().timestamp())-((15 + 15) * 60000)
# myquery = [{"updt": {"$gt":qtime2,'$lt':qtime}}, {"$group": {"_id": {"event": "$eventId", "market": "$marketId", "sign": "$signId"}}}]
# mydoc = mycol.aggregate(myquery)
l = []
# for x in mydoc:
#     print(x)
# print(len(l))


# mydoc = mycol.aggregate([
#   {
#     "$match" : { "updt": { "$gte": qtime2, "$lt": qtime } }
#   },
#     {
#    "$group": {
#       "_id": {
#          "event": "$eventId", "market": "$marketId", "sign": "$signId",
#          }
#       }
# },
#    {"$match":

#       {
#          "eventId" :"event" ,"marketid" : "market", "signId":"sign"

#       }


#    }])

mydoc = mycol.aggregate( [
   {
     "$bucketAuto": {
         "groupBy": "$eventId",
         "buckets": 4
     }
   }
] )
# print(mydoc)
for x in mydoc:
   print(x) 