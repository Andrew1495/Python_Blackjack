from modules import card_list
from modules import card_shuffle_and_deal

deck = card_list.cards

player_chips = 5000

computer_hand = card_shuffle_and_deal.dealing_hand(deck,51)

player_hand = card_shuffle_and_deal.dealing_hand(deck,49)

