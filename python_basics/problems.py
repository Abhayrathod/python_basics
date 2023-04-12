# Finding the percentage

# n = int(input())
# student_marks = {}
# for i in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# marks=student_marks[query_name]
# print(format(sum(marks)/3,'.2f'))


#LIST

# lst = []
# n = int(input())
# for i in range(n): #insert 0 10
#     cmd = input().split()
#     if cmd[0] == "insert":
#         lst.insert(int(cmd[1]), int(cmd[2]))
#     elif cmd[0] == "print":
#         print(lst)
#     elif cmd[0] == "append":
#         lst.append(int(cmd[1]))
#     elif cmd[0] == "sort":
#         lst.sort()
#     elif cmd[0] == "pop":
#         lst.pop()
#     elif cmd[0] == "remove":
#         print(cmd[1])
#         lst.remove(int(cmd[1]))
#     else:
#         lst.reverse()


#WHATS YOUR NAME?

# def print_full_name(first, last):
#     print("Hello "+first+" "+last+"!"+" You just delved into python.")

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)



#STRING MUTATIONS

# def mutate_string(string, position, character):
#     return string[:position]+character+string[position+1:]

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)



#STRING VALIDATORS

# if __name__ == '__main__':
#     s = input()
#     print(any([i.isalnum() for i in s]))
#     print(any([i.isalpha() for i in s]))
#     print(any([i.isdigit() for i in s]))
#     print(any([i.islower() for i in s]))
#     print(any([i.isupper() for i in s]))

# TEXT ALIGNMENT

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#TEXT WRAP

# import textwrap

# def wrap(string, max_width):
#     return textwrap.fill(string,max_width)

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)