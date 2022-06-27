# l = int(input("Enter the lenght of cuboid :"))
# b = int(input("Enter the breadth of cuboid :"))
# h = int(input("Enter the height of cuboid :"))
# print("the volume of a cuboid is :",l*b*h)

# print("the volume of a cuboid is :",int(input("Enter the length :"))*int(input("Enter the breadth :"))*int(input("Enter the height :")))  #---- alternate way

#----------------------------alternate way using function-----------------
def volume(l,b,h):
    volume = l*b*h
    return volume
find_volume = volume(int(input("Enter the length :")),int(input("Enter the breadth :")),int(input("Enter the height :")))
print("The volume of cuboid is :",find_volume)