from modules.card_list import *
from modules.card_shuffle_and_deal import *
from modules.hand_values import *

deck = shuffle_deck(cards)
upper_range = size_of_deck(deck)

does_player_want_to_play = input("Would you like to play a game of blackjack?\nyes/no\n".lower())
while does_player_want_to_play != "yes" and does_player_want_to_play != "no":
    does_player_want_to_play = input("Would you like to play a game of blackjack ?\nplease awnser yes/no\n".lower())
if does_player_want_to_play == "no":
    quit()


computer_hand = dealing_hand(deck, upper_range)
upper_range = size_of_deck(deck)
player_hand = dealing_hand(deck, upper_range)
upper_range = size_of_deck(deck)

player_has_ace = does_hand_ace(player_hand)
computer_has_ace = does_hand_ace(computer_hand)
player_hand_value = hand_value(player_hand, player_has_ace)
computer_hand_value = hand_value(computer_hand, computer_has_ace)

print("\n \n")
print(f"your hand is:\n{player_hand[0]['name']} and {player_hand[1]['name']}\nyour hand is valued at: {player_hand_value}")

if player_hand_value == 21 and computer_hand_value == 21:
    print("You both have blackjack, its a draw")
    quit()
elif player_hand_value == 21:
    Print("You have blackjack, you win!")
    quit()
elif computer_hand_value == 21:
    print("Unlucky, The dealer has blackjack, you lose")
    quit()



print("\n")
print(f"the dealer is currently showing a {computer_hand[1]['name']}")
print("\n")
hit_or_stick = input("Would you like to hit or stick? \nhit/stick\n".lower())
while hit_or_stick != "hit" and hit_or_stick != "stick":
    hit_or_stick = input("Would you like to hit or stick? \nhit/stick\n".lower())
# print(player_hand,computer_hand,upper_range)

# player_has_ace = does_hand_ace(player_hand)
# computer_has_ace = does_hand_ace(computer_hand)

# print(player_has_ace, computer_has_ace)

# player_hand_value = hand_value(player_hand, player_has_ace)
# computer_hand_value = hand_value(computer_hand, computer_has_ace)

# print("this is your hand value",player_hand_value)
# print(player_hand)
# print("this is computer hand value",computer_hand_value)
# print(computer_hand)

# hitting(deck, upper_range, player_hand)
# player_hand_value = hand_value(player_hand, player_has_ace)
# print("this is player hand",player_hand)
# print("player hand value is",player_hand_value)


# winner = compare_hands(player_hand_value, computer_hand_value)
# print(winner)