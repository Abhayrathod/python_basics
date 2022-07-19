class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        '''This function will print all the details 
        of the instance of class Employee '''
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")
print(harry.printdetails())
# print(Employee.printdetails.__doc__)
# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# print(harry.salary)
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
# print(rohan.printdetails())

# print(harry.salary)



class Student():
    student_strength = 34

    def __init__(self,sname,smarks):
        self.name = sname
        self.marks = smarks

    def printdet(self):
        return f"name is {self.name} and marks is {self.marks}"

abhay = Student("abhay",90)
print(abhay.printdet())