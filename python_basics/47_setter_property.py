
class Employee:
    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname
        # self.email = f"{self.fname} {self.lname} @outlook.com"

    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set."
        return f"{self.fname} {self.lname} @outlook.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

abhaysingh = Employee("abhay", "singh")
abhay2singh2 = Employee("abhay2", "singh2")
print(abhaysingh.email)
abhaysingh.fname = "new"
print(abhaysingh.email)
abhaysingh.email = "this.that@gmail.com"
print(abhaysingh.email)

del abhaysingh.email
print(abhaysingh.email)