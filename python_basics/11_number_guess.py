# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

# n=int(input("Enter the secret no"))
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :"))
#     if guess_number<n:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>n:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses you took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1

# if(number_of_guesses>9):
#     print("Game Over")
  

no_of_guess = 0
secret_number = int(input("Enter your secret number: "))
given_guesses = int(input("Enter the no of guesses you wanna provide to player: "))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
while no_of_guess < given_guesses:
    guess = int(input("Guess the number: "))
    no_of_guess+=1
    if guess < secret_number:
        print("The number you entered is lesser than the secret number")
    elif guess > secret_number:
        print("The number you entered is greater than the secret number")
    else:
        if no_of_guess<7:
            print("you are fucking probro69")
            print("you won\n")
            print(f"you took {no_of_guess} no of guesses to finish")
            break
    print("no of guess left is ", given_guesses - no_of_guess ,"\n")
if(no_of_guess == given_guesses):
    print("game over, YOU DUMB FOOL")
