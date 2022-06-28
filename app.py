from modules.player import Player
from modules.deck import Deck
from modules.card import Card
from modules.turn import *

card = Card(suit)
p1 = Player("Andrew")
p2_computer = Player("Computer")

print(p1.name,p2_computer.name)

deck = Deck()
deck.populate(card.Card)
deck.shuffle()



