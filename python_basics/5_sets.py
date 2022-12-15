#---------set is unordered, immutable, unindexed and duplicates are not allowed
# # s = set()
# print(type(s))
# l = [1, 2, 3, 4]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))
# s.add(1)
# s.add(4)
# s.add(1)
# s.add(2)
# s.remove(2)
# print(s)
# s1 = s_from_list.intersection({4,5})
# print(s_from_list,s1)
# print(s_from_list.isdisjoint(s1))

# set1 = {'apple','mango','banana','kiwi'}
# print(len(set1))
# list1 = ['new','old','blue']
# set1.update(list1)
# print(set1)
# dict1 = {"1":'old','2':'gold'}
# print(dict1)
# print(set(dict1))
# set1.update(dict1)
# print(set1)

#---------------------set comprehension-------------------------
# dresses = {dress for dress in ['dress1', 'dress1','dress2','dress2', 'dress3','dress3']}
# print(dresses)

#---------intialize empty set and adding values
# s = set()
# for i in range(1,100):
#     s.add(i)
# s.add(15)       # adding duplicate value but it will not show
# print(s)          #this is printing everything in order , dont know why


#------------made a list of 100 numbers and converted it to set but still it is printing in ordered way, find out why \
                # one of the reason being it is taking value as integer
# l = []
# for i in range(100):
#     l.append(i)

# print(l)
# s = set(l)
# a = "str" "fdg" 'sfsd'
# s.add(a)        # there is a difference in adding and updating , try it
# s.update(a)
# print(s)

# b = {1,2,3,4,5,6007,8,9,10,11,1200,13,14,15,16,17,18,19,20}
# print(b)
# a = {6,2,90,4,12,0,4000,345}
# print(a)
