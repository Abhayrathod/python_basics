# class Employee:
#     no_of_leaves = 8                # ye class variable hai
#     pass

# harry = Employee()
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(Employee.no_of_leaves)
# print(rohan.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.no_of_leaves)

# print(harry.__dict__)
# print(Employee.no_of_leaves)
# print(Employee.__dict__)



#--------------------------geeky shows

class Mobile():
    model = "mobile"            # ye class variable hai , class variable of instance variable me farq hota hai, 
                                # "YE EK CLASS NAMESPACE HAI", AGAR YE CHANGE HOGA TO EFFECT SB PAR AAYEGA

    # def __init__(self):         # instance variable
    #     self.model = "Instance Model"

    def show_model(self):       # instance method
        print("model is :",self.model)      # accessing instance variable

    @classmethod                # class method
    def is_model(cls):          # accessing class variable. not neccessarily 'cls' 
        print(cls.model)

abhay = Mobile()
honey = Mobile()

Mobile.model = "no model"
# honey.model = "honey_phone"
# print(Mobile.model)
print(abhay.model)
print(honey.model)

# Mobile.is_model()
# abhay.is_model()
# honey.is_model()

