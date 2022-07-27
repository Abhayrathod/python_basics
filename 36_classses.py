<<<<<<< HEAD
# class Student:
#     pass

# harry = Student()
# larry = Student()

# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)
# print(type(harry))



#geek shows 

class Player(object):
    def __init__(self,name):
        print("the name of the instance is:", name)
    def player_name(self,p):
        self.price = p
        print("player name is :",self.price)

abhay = Player("abhay")
abhay.player_name("also_abhay")
print(id(abhay))
print()

honey = Player("honey")
honey.player_name("also_honey")
print(id(honey))
print()

mayank = Player("mayank")
mayank.player_name("also_mayank")
print(id(mayank))
print()

class Student:
    pass

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.section, larry.subjects)
print(type(harry))
print(larry.subjects[1])
>>>>>>> af653441e1a88e56701bffeca7e06dfead464ee6
