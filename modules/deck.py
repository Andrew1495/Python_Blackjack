
from card import *
from random import *

class Deck:
    def __init__(self):
        self.cards_in_deck = []


    def populate(self):
        suits = ["hearts", "diamonds", "clubs","spades"]
        values = [
        {
            "name": "Ace",
            "value": 11
        },
        {
            "name": "2",
            "value": 2
        },
        {
            "name": "3",
            "value": 3
        },
        {
            "name": "4",
            "value": 4
        },
        {
            "name": "5",
            "value": 5
        },
        {
            "name": "6",
            "value": 6
        },
        {
            "name": "7",
            "value": 7
        },
        {
            "name": "8",
            "value": 8
        },
        {
            "name": "9",
            "value": 9
        },
        {
            "name": "10",
            "value": 10
        },
        {
            "name": "Jack",
            "value": 10
        },
        {
            "name": "Queen",
            "value": 10
        },
        {
            "name": "King",
            "value": 10
        },
        ]

        for suit in suits:
            for value in values:

                card = Card(suit)
                card.value["name"] = value["name"]
                card.value["value"] = value["value"]
                
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
