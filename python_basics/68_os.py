import os 

#printing os path
# a = os.getcwd()
# print(a)

#changing current os directory----------------------------

# def current_path():
#     print("current working directory:")
#     b = os.getcwd()
#     print(b)

# current_path()

# os.chdir('../')
# current_path()

#making directory--------------------------

# directory = 'abhay'

# parent_directory = 'E:/'

# path = os.path.join(parent_directory,directory)

# os.mkdir(path)
# print(os.getcwd())

#make directories will create all the directories if they don't exist------------------
# import os 

# direct = "abhay1"

# parent_dict = "E:/a/b/"

# np = os.path.join(parent_dict, direct)
# os.makedirs(np)

# print(os.getcwd())

#list directories in the folder-----------------------------------

# path = 'E:/'
# print(os.listdir(path))

#deleting file with os.remove-------------------check the code

# import os 

# file = 'file1.txt'
# location = "E:/abhay/"

# path = os.path.join(location, file)

# os.remove(path)

#deleting the directory using os.rmdir-------------------------

# import os 

# lo = "abhay"
# location = "E:/"
# path = os.path.join(location, lo)
# os.rmdir(path)

#get the os name------------------------------
import os

print(os.name())