import time

initial = time.time()
print(initial)
k = 0
while(k<45):
    print("this is a statement")
    time.sleep()
    k+=1
print("while loop ran in", time.time() - initial)

initial2 =time.time()
for i in range(45):
    print("this is also a statement")

print("for loop ran in", time.time() - initial2)


localtime = time.asctime(time.localtime(time.time()))
print(localtime)