#LEAP YEAR LOGIC ----> IF YEAR IS DIVISIBLE BY 400 THEN IT IS LEAP YEAR AND IF IT IS DIVISIBLE BY 4 BUT NOT 100 THEN IT IS LEAP YEAR



# year = int(input("Enter the year :"))
# if year%400==0 or (year%100!=0 and year%4==0):
#     print("{} is a leap year".format(year))
# else:
#     print("not leap year")

#-----------------------------alternate method by using function-------------------------------------method1
# def is_leap(year):
#     leap = False
#     if year%400==0:
#         leap = True
#     elif year%100==0:
#         leap = True
#     elif year%4==0:
#         leap = True
#     return leap

# is_leap(int(input("Enter the year :")))
# if is_leap==True:
#     print("leap year")
# else:
#     print("not a leap year")

#-----------------------------alternate method by using function-------------------------------------method2

# def checkYear(year):
# 	if (year % 4) == 0:
# 		if (year % 100) == 0:
# 			if (year % 400) == 0:
# 				return True
# 			else:
# 				return False
# 		else:
# 			return True
# 	else:
# 		return False

# if(checkYear(int(input("Enter the numbers :")))):
# 	print("Leap Year")
# else:
# 	print("Not a Leap Year")


#-----------------------------alternate method by using function-------------------------------------method3

# year = int(input('Enter year : '))
 
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
#     print(year, "is a leap year.")
# else :
#     print(year, "is not a leap year.")

#-----------------------------alternate method by using function-------------------------------------method4

# Python3 implementation to check if the year is a leap year using macros
# Macro to check if a year is a leap year

# def ISLP(y):
#     if ((y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0)):
#         return 1
#     else:
#         return 0

# year = int(input("Enter the year"))
# print(ISLP(year))

#-----------------------------alternate method by using function-------------------------------------method5

# def checkYear(year):
	
# 	# Return true if year is a multiple
# 	# of 4 and not multiple of 100.
# 	# OR year is multiple of 400.
# 	import calendar
# 	return(calendar.isleap(year))
	
# # Driver Code
# year = 2000
# if (checkYear(year)):
# 	print("Leap Year")
# else:
# 	print("Not a Leap Year")


#-----------------------------alternate method by using function-------------------------------------method6

# year = int(input("Enter a year: "))

# # divided by 100 means century year (ending with 00) , century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# # not divided by 100 means not a century year
# # year divided by 4 is a leap year
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# # if not divided by both 400 (century year) and 4 (not century year)
# # year is not leap year
# else:
#     print("{0} is not a leap year".format(year))

#-----------------------------alternate method by using function-------------------------------------method7

# x = int(input("Enter the year :"))
# result = "leap year" if x%400==0 else "Leap year" if x%4==0 and x%100!=0 else "not leap year"
# print(result)