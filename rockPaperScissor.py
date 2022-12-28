###############################################################################
#Rock paper scissor game. this program accepts user input and compares to computer's choice
# and decides who won. Scissor wins over paper, paper over rock, rock over scissor
#if its a draw or invalid input, prompt user for new input
#############################################################################################
import random

options = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
count = 0
letter,compChoice = random.choice(list(options.items()))

while count < 5: #give user 5 options to make a valid input
    choice = input('Please make a choice r for rock, p for paper and s for scissors \n')
    if len(choice)==0 or choice[0].lower() not in ['r', 'p', 's']:
        count += 1
        print(f'you have {5 - count} chances to make a valid input\n')
        if count == 5:
            print('Game ends')
            break
        continue
    else:
        userLetter = choice[0].lower()
        userChoice = options[userLetter]
    if compChoice != userChoice:
        if (userLetter == 'r' and letter == 's') or (userLetter == 's' and letter == 'p') or (userLetter == 'p' and letter == 'r'):
            print(f'You win!!! You chose {userChoice} and computer chose {compChoice}')
            break
        else:
            print(f'You lost!!! You chose {userChoice} and computer chose {compChoice}')
            break
    else:
        print(f'Draw!!! You chose {userChoice} and computer chose {compChoice}')

