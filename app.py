from modules import card_list
from modules import card_shuffle_and_deal

deck = card_shuffle_and_deal.shuffle_deck(card_list.cards)

player_chips = 5000

upper_range = card_shuffle_and_deal.upper_range(deck)
print(upper_range)
computer_hand = card_shuffle_and_deal.dealing_hand(deck,upper_range)
upper_range = card_shuffle_and_deal.upper_range(deck)
player_hand = card_shuffle_and_deal.dealing_hand(deck,upper_range)
upper_range = card_shuffle_and_deal.upper_range(deck)

print(upper_range)