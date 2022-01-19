from random import *
def win():
    print ('You win!')
def lose():
    print ('You lose!')
a=True
while a:
    player_choice = input('What do you pick? (rock, paper, scissors):')
    # random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    random_move = randint(0, 2)
    computer_choice=moves[random_move]
    # computer_choice = [random_move]
    if player_choice == computer_choice:
        print ('Draw!')
        a=False
    elif  player_choice=='rock' and computer_choice == 'scissors':
        win()
        a=False
    elif   'paper'==player_choice and computer_choice == 'scissors':
        lose()
        a=False
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
        a=False
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
        a=False
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
        a=False
    elif player_choice == 'paper' and computer_choice == 'scissors':
        lose()
        a=False
    again = input('Do you want to play again? (y or n):').strip()
    if again == 'y':
        a=True
    elif again=='n':
        a=False



