# Types of methods

# 1. Instance methods
#     - Ancessor methods/Getter Method
#     - Mutator methods/Setter Method

        # Notes - 1 - Instance methods ko instance objects se call kar skte hai kyuki vo use hi juda hota hai
                # 2 -  

# 2. class Methods

# 3. Static methods

#-----------1 Instance method
# class Mobile:
#     # Instance method
#     def show_model(self, p ):       # with parameter
#         self.price = p
#         print("instance model")
#         print(self.price)

# abhay = Mobile()
# honey = Mobile()
# mayank = Mobile()

# abhay.show_model(1000)

#------------1 Instance Method - Getter method - method is used to read or access data
# general syntax, not compulsory - def get_value(self)
                                # -   def get_result(self)
                                # -   def get_name(self)
                                # -   def get_id(self)




# class Mobile2():
#     def __init__(self):
#         self.model = "Realme X"

#     def get_model(self):
#         return self.model

# abhay = Mobile2()
# m = abhay.get_model()
# print(m)

#------------1 Instance Method - Setter method - method is used to create data

# class Mobile3():
#     def __init__(self):
#         self.model = "no Model"

#     def set_model(self,m):
#         self.model = m
#         print("model is assigned")

# abhay = Mobile3()
# abhay.set_model("New data")
# print(abhay.model)


#-----------------------------2. Class method

# class Mobile4():
#     abc = "abhay"
    
#     @classmethod
#     def show_name(nan):
#         print(nan.abc)

# abhay = Mobile4()
# a = abhay.show_name()
# print(a)


#-----------------------------3. static methods

class Mobile5():
    @staticmethod
    def show_model(m,p):
        model = m 
        price = p
        print("model")

abhay = Mobile5()
abhay.show_model("new",900)