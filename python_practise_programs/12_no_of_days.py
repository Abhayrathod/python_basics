#------------------------find no of days in a momth-----------------------
# class Solution(object):
#    def numberOfDays(self, y, m):
#       leap = 0
#       if y% 400 == 0:
#          leap = 1
#       elif y % 100 == 0:
#          leap = 0
#       elif y% 4 == 0:
#          leap = 1
#       if m==2:
#          return 28 + leap
#       list = [1,3,5,7,8,10,12]
#       if m in list:
#          return 31
#       return 30
# ob1 = Solution()
# print(ob1.numberOfDays(int(input(("Enter the year :"))), int(input("Enter the month no :"))))


#------------------------no of days between two dates-----------------------

# from datetime import date

# date1 = date(2016,1,20)
# date2 = date(2017,1,20)
# days = (date2 - date1).days
# print(days)

#------------------------no of days between two dates without using function-----------------------

