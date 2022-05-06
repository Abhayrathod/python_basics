from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def printarea(self):
        return f"The area of the rectangle is {self.length * self.breadth}"

rect = Rectangle(int(input("Etner the length of the rectangle: ")), int(input("Enter the breadth of the rectangle: ")))
print(rect.printarea())
# newobj = Shape()    # cant allow to make object from abstract base class
    