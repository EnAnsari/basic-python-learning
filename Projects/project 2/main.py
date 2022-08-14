# part 17 from 97
# project 2
# Rock, Paper, Scissors

import random

print('Rock...')
print('Paper...')
print('Scissors...\n')

randomNumber = random.randint(0, 2)

if randomNumber == 0:
    computerMove = 'rock'
elif randomNumber == 1:
    computerMove = 'paper'
else:
    computerMove = 'scissors'

player_1 = input("player_1, Make your move : ").lower()
print(f"player_2, Make your move : {computerMove}")
player_2 = computerMove

if player_1 == player_2:
    print("that's a tie!")
elif player_1 == 'rock':
    if player_2 == 'scissors':
        print('player_1 wins!')
    else:
        print('player_2 wins!')
elif player_1 == 'paper':
    if player_2 == 'scissors':
        print('player_2 wins!')
    else:
        print('player_1 wins!')
elif player_1 == 'scissors':
    if player_2 == 'paper':
        print('player_1 wins!')
    else:
        print('player_2 wins!')
else:
    print("something went wrong!")

