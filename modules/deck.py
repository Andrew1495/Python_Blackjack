
from card import *
from random import *

class Deck:
    def __init__(self):
        self.cards_in_deck = []


    def populate(self):
        suits = ["hearts", "diamonds", "clubs","spades"]
        values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards_in_deck.append(card)



    def shuffle(self) :
        for index in range (len(self.cards_in_deck)-1,0,-1):
            random_index = randint(0 , index)
            self.cards_in_deck[index],self.cards_in_deck[random_index] = self.cards_in_deck[random_index] , self.cards_in_deck[index]


    def display_deck(self):
        for card in self.cards_in_deck:
            card.print_card()


deck = Deck()
deck.populate()
deck.shuffle()
deck.display_deck()
