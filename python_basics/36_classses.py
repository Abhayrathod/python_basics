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
# print(type(Student))
# print(larry.subjects[1])



#geek shows 
#--------------------------constructor with parameter 
class Player():
    def __init__(self,name):
        self.name = name        # ye instance variable hai
        # print("the name of the instance is:", name)
    def player_name(self,p):                # is method ko instance method bolte hai\
        self.salary = p
        print("the salary is ",p)
        print(self.name)        # ye instance variable ko access kar rahe hai instance method k through

abhay = Player("abhay")
# abhay.player_name("also_abhay")
abhay.player_name("300000")
abhay.name = "fsdhbvshd"
abhay.salary = 300000
print(abhay.name)
print(abhay.__init__("new"))
print(id(abhay))
print()

honey = Player("honey")
honey.player_name("also_honey")
print(id(honey))
print()

# mayank = Player("mayank")
# mayank.player_name("also_mayank")
# print(id(mayank))
# print()

#------------------------constructor with parameter

# class NewPlayer:
#     def __init__(self):
#         print("this init method/constructor is automatically run")

# new = NewPlayer()
