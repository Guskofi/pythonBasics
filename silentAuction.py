########################################################
# This program asks users to input their name and bid amount,
# stores them in a dictionary till there are no users.
# then it selects the winning bid
#########################################################

Bidders = {}
newPlayer = True


#############################################
# this function block accepts users bid. after 2 failed attempts user is assigned $0 bid
##############################################

def add_bids():
    bid_chance = 2
    while bid_chance > 0:
        if bid_chance == 0:
            print('You failed to place a bid\n ')
            bid = 0
            break
        try:
            bid = int(input('Please enter your bid $'))
            break
        except ValueError:
            bid_chance -= 1
            print(f'Please enter an integer, you have {bid_chance} chances left')
    return bid


#############################################
# this function block accepts users name. after 2 failed attempts user is assigned no name
##############################################

def add_player():
    chance = 2
    while chance > 0:
        name = input(f'Please enter the your name on ID\n ')
        if len(name) != 0:
            break
        else:
            chance -= 1
            if chance == 0:
                print('You cant play without a name\n')
                break
            else:
                print(f'You have {chance} chances left\n')
    return name


#############################################
# this loop asks for name and bid till their is no new input
# if no name or name is already taken it, it prints invalid name
# bids are only accepted if name is valid
##############################################
next_player = True
while next_player:
    player_name = add_player()
    if player_name == '' or player_name in Bidders.keys():
        print('Name Invalid or name already taken')
    else:
        player_bid = add_bids()
        Bidders[player_name] = player_bid
    newPlayer = input('any new player available? answer yes or no ')
    if newPlayer.lower() == 'no':
        next_player = False

#############################################
# this block finds the winning bid and selects the first person with that bid.
##############################################
# sorted_Bidders = sorted(Bidders.items(), key=lambda kv: kv[1])
if len(Bidders) > 0:
    winning_bid = max(Bidders.values())
    for k, v in Bidders.items():
        if v == winning_bid:
            winner = k
            break
        else:
            pass
    print(f'{winner} gave us the winning bid of ${winning_bid}')
else:
    print('sorry no bids received ')
