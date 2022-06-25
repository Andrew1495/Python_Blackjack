import random
# function to deal two cards based on random number to either computer or player,
# it will remove the cards from the list after they have been selected
# upper range must be set so after a card is removed the range will be p=one smaller


def dealing_hand(deck, upper_range):
    hand = []
    counter = 2
    while counter > 0:
        picking_card = random.randint(0, upper_range)
        hand.append(deck[picking_card])
        deck.pop(picking_card)
        upper_range -= 1
        counter -= 1
    return  hand


# will append a new card into current hand
# upper_range must be modified to make sure there are no repeats

def hitting(deck,upper_range,hand):
    picking_card = random.randint(0, upper_range)
    hand.append(deck[picking_card])
    deck.pop(picking_card)
    

# function allows the top range of the deck to be change after each card is taken out
# it might be better to use range but for now this will work

def upper_range(deck):
    return len(deck)
