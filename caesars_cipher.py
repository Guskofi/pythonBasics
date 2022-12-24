#This program is caesars code. the goal of the program is to decode or encode a
# Give the user 3 chances to state his purpose if it fails
chance = 3
while chance > 0:
    action = input('What do you want to do? decode or encode ')
    if action.lower()  in ['decode', 'encode']:
        break
    else:
        chance -= 1
        if chance == 0:
            print('You got killed by spies\n')
            break
        else:
            print(f'You have {chance} chances left before spies find you\n')

#give the user 5 chances to enter their message
chance = 5
while chance > 0:
    raw_message = input(f'Please enter the phrase you want to {action} ')
    if len(raw_message) != 0:
            break
    else:
        chance -= 1
        if chance == 0:
            print('You got killed by spies\n')
            break
        else:
            print(f'You have {chance} chances left before spies find you\n')

#Give user 3 options to enter shift index
chance = 3
while chance > 0:
    if chance == 0:
        print('You got killed by Spies ')
        break
    try:
        shift = int(input('Please enter shift index '))
        break
    except ValueError:
        chance-=1
        print(f'Please enter an integer, you have {chance} chances left')


def caesars_code (input, action, shift):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    output = ''
    for char in input:
        if char not in letters:
            coded_letter = char
        else:
            for position in range(len(letters)):
                if char == letters[position]:
                    if action == 'encode':
                        coded_letter = letters[(position + shift) % 26]
                    else:
                        coded_letter = letters[position - (shift % 26)]
            else:
                pass
        output += coded_letter
    return output

print(caesars_code (raw_message, action, shift))
