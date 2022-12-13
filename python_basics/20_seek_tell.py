f = open("harry.txt","r+")
l = ["this is just an scrap data"]
f.writelines(l)
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.tell())
f.close()
  
