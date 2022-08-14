# part 20 from 97
# project 3
# Rock, Paper, Scissors by 3 score


import random

print('Rock...')
print('Paper...')
print('Scissors...\n')

player_1_wins = player_2_wins = 0
winning_score = 3

while player_1_wins < winning_score and player_2_wins < winning_score:
    randomNumber = random.randint(0, 2)

    if randomNumber == 0:
        computerMove = 'rock'
    elif randomNumber == 1:
        computerMove = 'paper'
    else:
        computerMove = 'scissors'

    print(f'\nplayer 1 : {player_1_wins} and player 2 : {player_2_wins}')
    player_1 = input("player_1, Make your move : ").lower()
    if(player_1 == 'q' or player_1 == 'quit'):
        break
    print(f"player_2, Make your move : {computerMove}")
    player_2 = computerMove

    if player_1 == player_2:
        print("that's a tie!")
    elif player_1 == 'rock':
        if player_2 == 'scissors':
            print('player_1 wins!')
            player_1_wins += 1
        else:
            print('player_2 wins!')
            player_2_wins += 1
    elif player_1 == 'paper':
        if player_2 == 'scissors':
            print('player_2 wins!')
            player_2_wins += 1
        else:
            print('player_1 wins!')
            player_1_wins += 1
    elif player_1 == 'scissors':
        if player_2 == 'paper':
            print('player_1 wins!')
            player_1_wins += 1
        else:
            print('player_2 wins!')
            player_2_wins += 1
    else:
        print("something went wrong!")

if player_1_wins == winning_score:
    print('\nplayer 1 is winner!')
else:
    print('\nplayer 2 is winner!')