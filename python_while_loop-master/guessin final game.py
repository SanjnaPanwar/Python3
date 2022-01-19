
number_to_guess = int(input("What should the number_to_guess be...:? "))
guesses = int(input("How many guesses.:? "))

guess_any_num = 0
user_guess = int(input("Guess a number: "))
guess_any_num += 1
if number_to_guess < user_guess:
    print("The number is lower than that.")
elif number_to_guess > user_guess:
    print("The number is higher than that")

while user_guess !=number_to_guess and guess_any_num < guesses:
    user_guess = int(input("Guess a number: "))
    guess_any_num += 1
    if number_to_guess < user_guess:
        print("The number is lower than that.")
    elif number_to_guess > user_guess:
        print("The number is higher than that")

if guess_any_num >= guesses and user_guess !=number_to_guess:
    print("You lose; the number was ", number_to_guess)
if user_guess ==number_to_guess:
    print(" WOW..You guess right number...win!")