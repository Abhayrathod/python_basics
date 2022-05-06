#range(start,stop,stepsize)
# all arguments must be integer - positive or negative whatever
# stepsize cannot be zero
#only stop value is mandatory

a = range(1,8,2)
#JO RANGE GENERATE HOGI UNKA APNA EK INDEX No HOGA
#JESE UPR 0-5 TK No GENERATE HOGA TO 0 KI INDEX 0 OR 1 KI 1
#AGAR No 2-10 TAK GENERATE HOGA TO 2 KI INDEX 0 HOGI OR 3 KI 1 PHR 4 KI 2 AND SO ON
#JRURI NAHI 0 HAI TO INDEX BHI O HO
#AGAR STEPSIZE DE DIYA TO NO ALAG HONGE LEKIN INDEX TO O SE HI START HOGA

print(a[2])
for i in a :
    print(i)