import time

# initial = time.time()
# print(initial)
# k = 0
# while(k<30):
#     print("this is inside a while loop")
#     # time.sleep(1)
#     k+=1
# print("while loop ran in", time.time() - initial)

# initial2 =time.time()
# for i in range(30):
#     print("this is inside a for loop")

# print("for loop ran in", time.time() - initial2)


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

#----------epoch - epoch is where the time starts and is platform-dependent and mostly it starts from jan 1 1970
# print(time.gmtime()) #----provides epoch time 


# # print(time.ctime()) #-- takes argument  is seconds and convert the time from epoch to the metioned time in argment 
# # print(time.localtime()) #-- provides a current time but in struct time format
# # print(time.time()) #----also provides current time but in seconds from epoch , i guess
# # print(time.asctime()) #----provides time but in systematic format
# # obj1 = time.gmtime()
# # print(time.mktime(obj1))


# # using simple format of showing time
# s = time.strftime("%a, %d %b %Y %H:%M:%S",
# 			time.gmtime(1627987508.6496193))
# print(s)


# #--------Converting tuple to time.struct_time object to string

# obj = time.gmtime(1627987508.6496193)

# # Convert the time.struct_time object to a 
# # string of the form 'Day Mon Date Hour:Min:Sec Year' using time.asctime() method
# time_str = time.asctime(obj)
# print(time_str)


# obj = time.localtime(1627987508.6496193)

# # Convert the time.struct_time
# # object to a string of the
# # form 'Day Mon Date Hour:Min:Sec Year'
# # using time.asctime() method
# time_str = time.asctime(obj)
# print(time_str)


#--------time.strptime() method converts the string representing time to the struct_time object.
# string = "Tue, 03 Aug 2021 10:45:08"
# obj = time.strptime(string, "%a, %d %b %Y %H:%M:%S")

# print(obj)
