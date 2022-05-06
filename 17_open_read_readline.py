#harry code
# # f = open("myfile_16.txt", "r")
# a = f.read(24)  # Here, you will get the first two characters of the file.
# print(a)

# f = open("myfile_16.txt", "r")
# a = f.readlines()  # Returns a list object
# print(a)
# f.close()

# f = open("abhay_21.txt", "rt")
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
# #
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
# #
# content = f.read(34455)
# print("2", content)
# f.close()



# self written code

# myfile1 = open("myfile.txt","w")
# l = ["this is me \n", "this is us\n","this is my party\n"]
# myfile1.write("Hello\n")
# myfile1.writelines(l)
# myfile1.close()
# myfile1 = open("myfile.txt","r+")
# print('output of read function is')
# print(myfile1.read())
# print()
# myfile1.seek(0)
# print("output of readline function is ")
# print(myfile1.readline())
# print()
# myfile1.seek(0)
# print("output of read(9) function is ")
# print(myfile1.read(9))
# print()
# myfile1.seek(0)
# print("output of the readline(9) function is ")
# print(myfile1.readline(9))
# print()
# myfile1.seek(0)
# print("output of the readlines funtion is ")
# print(myfile1.readlines())
# print()
# myfile1.close()



# appending vs write mode
# print("writing file in write mode")
# myfile1 = open("myfile.txt","w")
# l = ["This is me\n", "this is us\n","this is our party\n"]
# myfile1.writelines(l)
# myfile1.close()
# #Appends- adds at last
# myfile1 = open("myfile.txt","a")
# myfile1.write("this is append data\n")
# myfile1.close()
# #opening file in read mode
# myfile1 = open("myfile.txt","r")
# print("output of the readlines after appending")
# print(myfile1.readlines())
# myfile1.close()
# #write -overwrites
# myfile1 = open("myfile.txt","w")
# myfile1.write("this is write")
# myfile1.close()
# #opening file after write mode 
# myfile1 = open("myfile.txt","r")
# print("opening file data after using write mode")
# print(myfile1.readlines())
# print()
# myfile1.close()

