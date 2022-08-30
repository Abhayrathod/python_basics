import pymongo
import datetime

dburl = "mongodb://localhost:27017/"
myclient = pymongo.MongoClient(dburl)

mydb = myclient["Betfair"]
mycol = mydb["betfair"]

mycol.create_index( [("updt", -1)] )

def getbackOdd(eventId,marketId,signId,time= None):
    if time:
        qtime = int(datetime.datetime.now().timestamp()) -(time * 60000)
        qtime2 = int(datetime.datetime.now().timestamp())-((time + 15) * 60000)

        myquery = [ { "eventId": eventId,"marketId":marketId,"signId":signId,"updt": {"$gt":qtime2,'$lt':qtime}}]
    else:
        myquery = { "eventId": eventId,"marketId":marketId,"signId":signId,"updt": int(datetime.datetime.now().timestamp())}

    mydoc = mycol.find_one(myquery,sort=[( 'updt', pymongo.DESCENDING,)])
    if mydoc:
        return mydoc["backOdd"]    
    else:
        return None  



def getResult(eventId,marketId,signId):

    return_obj = {}
    return_obj["signId"] = signId
    return_obj["marketId"] = marketId
    return_obj["eventId"] = eventId
    return_obj["odd"] = getbackOdd(eventId,marketId,signId)
    return_obj["odd-15"] = getbackOdd(eventId,marketId,signId,15)
    return_obj["odd-30"] = getbackOdd(eventId,marketId,signId,30)
    return_obj["odd-45"] = getbackOdd(eventId,marketId,signId,45)
    return_obj["odd-60"] = getbackOdd(eventId,marketId,signId,60)
    return_obj["odd-75"] = getbackOdd(eventId,marketId,signId,75)
    return_obj["odd-90"] = getbackOdd(eventId,marketId,signId,90)
    return_obj["odd-105"] = getbackOdd(eventId,marketId,signId,105)
    return_obj["odd-120"] = getbackOdd(eventId,marketId,signId,120)
    return_obj["odd-135"] = getbackOdd(eventId,marketId,signId,135)
    return_obj["odd-150"] = getbackOdd(eventId,marketId,signId,150)
    return_obj["odd-165"] = getbackOdd(eventId,marketId,signId,165)
    return_obj["odd-180"] = getbackOdd(eventId,marketId,signId,180)
    return_obj["odd-195"] = getbackOdd(eventId,marketId,signId,195)
    return_obj["odd-210"] = getbackOdd(eventId,marketId,signId,210)
    return_obj["odd-225"] = getbackOdd(eventId,marketId,signId,225)
    return_obj["odd-240"] = getbackOdd(eventId,marketId,signId,240)
    return_obj["odd-255"] = getbackOdd(eventId,marketId,signId,255)
    return_obj["odd-270"] = getbackOdd(eventId,marketId,signId,270)
    return_obj["odd-285"] = getbackOdd(eventId,marketId,signId,285)
    return_obj["odd-300"] = getbackOdd(eventId,marketId,signId,300)
    print(return_obj)
    return return_obj

print(getResult(32986793,1,3))