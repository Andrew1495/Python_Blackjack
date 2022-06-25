from modules.card_list import *
from modules.card_shuffle_and_deal import *
from modules.hand_values import *

deck = shuffle_deck(cards)
upper_range = size_of_deck(deck)



computer_hand = dealing_hand(deck, upper_range)
upper_range = size_of_deck(deck)
player_hand = dealing_hand(deck, upper_range)
upper_range = size_of_deck(deck)

print(player_hand,computer_hand,upper_range)

player_has_ace = does_hand_ace(player_hand)
computer_has_ace = does_hand_ace(computer_hand)

print(player_has_ace, computer_has_ace)

player_hand_value = hand_value(player_hand, player_has_ace)
computer_hand_value = hand_value(computer_hand, computer_has_ace)

print("this is your hand value",player_hand_value)
print(player_hand)
print("this is computer hand value",computer_hand_value)
print(computer_hand)

winner = compare_hands(player_hand_value, computer_hand_value)
print(winner)