def simple_interest(p,t,r):
    si = (p*t*r)/100
    return si

print(simple_interest(int(input("principal :")),int(input("rate :")),int(input("time :"))))