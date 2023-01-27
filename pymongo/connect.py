from gettext import find
import pymongo



def insertDocument():
    studentInfo = {
        "name": "Drake",
        "section": 2,
        "maths_marks": 35,
        "sst_marks": 79
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(f"Student with id {student_id} has been created")


def readDocuments():
    # Inserting a Document
    # Reading a Collection
    # Using find function 
    myStudents = collection.find({"section": 1, "name": "Harry"})
    # print(myStudents)
    for student in myStudents:
        print(student)
    # Using findOne function 
    myStudent = collection.find_one({"section": 1})
    print(myStudent)


def updateDocuments():
    collection.update_one({"section": 1}, {'$inc': {'section': 100}})
    collection.update_many({}, {'$inc': {'section': 100}})


def deleteDocuments():
    r = collection.delete_one({"section": 101})
    print(r.deleted_count)
    r = collection.delete_many({"section": 101}) #this will delete all with section 101
    print(r.deleted_count)
    r = collection.delete_many({})      # not giving any argument means it will delete everything in database
    print(r.deleted_count)

if __name__ == "__main__":

    #-------------------------for connecting in local----------------------------------------------------------------------
    client = pymongo.MongoClient('localhost',27017)
    db =  client['test-db']
    collection = db['test-collection']
    print(collection)
    posts = db.posts
    post_id = posts.insert_one({"p":1}).inserted_id
    print(post_id)

    #-------------------------for connecting with mongo db atlas-----------------------------------------------------------

    connectionString = 'mongodb+srv://test-db:Abhay%23521821@cluster0.ha3glfk.mongodb.net/test'

    client = pymongo.MongoClient(connectionString)
    # creating a Database for School
    db = client['WisdomAcademy']             # dont put space between two database name else it will throw an error

    # Creating a collection
    collection = db.class1

    # Inserting a collection
    # insertDocument()

    #Reading a collection
    # readDocuments()

    #update the collection
    # updateDocuments()

    #delete the collection
    # deleteDocuments()