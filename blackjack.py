import random

def deal_card(old_cards_left):
    new_cards_left = []
    chosen_card = random.choice(old_cards_left)
    for element in old_cards_left:
        if element != chosen_card:
            new_cards_left.append(element)
        else:
            pass
    return chosen_card,new_cards_left

def hand_value(_card):
    rank, valued = _card
    if valued in ['a','j','q','k']:
        if valued == 'a':
            temp_card_value = 11
        else:
            temp_card_value = 10
    else:
        temp_card_value = int(valued)
    return temp_card_value
def check_for_ace(givenhand):
    a_count = 0
    for item in givenhand:
        if item[1] == 'a':
            a_count += 1
        else:
            pass
    return a_count


##################################################################################
# Draw out cards and create the necessary variables for the decision making process
##################################################################################
cards = {'diamond':[2,3,4,5,6,7,8,9,10,'j','q','k','a'],'heart':[2,3,4,5,6,7,8,9,10,'j','q','k','a'],'spades':[2,3,4,5,6,7,8,9,10,'j','q','k','a'],'club':[2,3,4,5,6,7,8,9,10,'j','q','k','a']}
cardlist = []
used_cards = []

for rank in list(cards.keys()):
    for card in cards[rank]:
        cardlist.append((rank,card))
#Round1
players_hand = []
dealers_hand = []
players_tot = 0
dealers_tot = 0
check_player_ace = 0
check_dealer_ace = 0
player_hit = True
player_stand = False
bust = False
############################################################################
#Give cards out, one for each player till both have 2
#check to see if player/dealer total hand is above 21, then reduce value one of the aces
#print both players card but only one of the dealer
###########################################################################
for number in range(1,5):
    if number%2 == 1:
        if number == 1:
            players_card, remaining_cards = deal_card(cardlist)
        else:
            players_card, remaining_cards = deal_card(remaining_cards)
        players_card_value = hand_value(players_card)
        players_hand.append(players_card)
        players_tot += players_card_value
        if players_tot > 21:
            players_tot-=10
            check_player_ace = 1
    else:
        dealers_card, remaining_cards = deal_card(remaining_cards)
        dealers_card_value = hand_value(dealers_card)
        dealers_hand.append(dealers_card)
        dealers_tot+= dealers_card_value
        if dealers_tot > 21:
            dealers_tot-=10
            check_dealer_ace = 1


print(f'players_hand is {players_hand} making a total of {players_tot}')
print(f'Dealers first card is {dealers_hand[0]}')

#########################################################################
#check to see if player had a natural (total = 21) then check same for dealer
#to decide who won the
#########################################################################

if players_tot == 21 or dealers_tot == 21:
    if players_tot > dealers_tot:
        print('natural, player wins')
    elif players_tot < dealers_tot:
        print('natural, Dealer wins')
    else:
        print('Draw')
    print(f'dealers_hand is {dealers_hand} making a total of {dealers_tot}')
    player_hit = False
    player_stand = False

############################################################################
#give the player an opportunity to decide if hit or stand
#if his total goes above 21 he's bust else he continues to decide hit or stand
#we account for aces by checking if hes drawn new ace or not. old aces are already taken care of
##############################################################################
while player_hit:
    player_move = input('hit or stand: ')
    if player_move.lower() != 'hit':
        player_hit = False
        player_stand = True
    else:
        players_card, remaining_cards = deal_card(remaining_cards)
        players_card_value = hand_value(players_card)
        players_hand.append(players_card)
        print(players_hand)
        players_tot += players_card_value
        if players_tot > 21:
            aces = check_for_ace(players_hand)
            if aces - check_player_ace > 0:
                players_tot -=10
                check_player_ace +=1
            else:
                print('Player bust')
                player_hit = False
                player_stand = False
                bust = True
        print(players_tot)
################################################################################
#if a player takes a stand dealer must show his cards. As long as his total card value is < 16, he has to take new cards till
# he burst or get higher than 16
# already drawn aces are taken care of
################################################################################
while player_stand:
    print(f'dealers_hand is {dealers_hand} making a total of {dealers_tot}')
    if dealers_tot > players_tot:
        player_stand = False
    elif dealers_tot > 16:
        player_stand = False
    else:
        dealers_card, remaining_cards = deal_card(remaining_cards)
        dealers_card_value = hand_value(dealers_card)
        dealers_hand.append(dealers_card)
        dealers_tot += dealers_card_value
        if dealers_tot > 21:
            num_ace = check_for_ace(dealers_hand)
            if num_ace - check_dealer_ace > 0:
                dealers_tot -=10
                check_dealer_ace+=1
            else:
                print(f'dealers_hand is {dealers_hand} making a total of {dealers_tot}')
                print('Dealer bust')
                player_decision = False
                player_stand = False
                bust = True


if bust:
    pass
else:
    if players_tot == dealers_tot:
        print('Draw')
    else:
        if players_tot > dealers_tot:
            print(f'Player wins!!!')
        else:
            print(f'Dealer wins!!!')






