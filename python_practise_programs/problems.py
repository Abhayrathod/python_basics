





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