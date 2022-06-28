class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.take_one())

    def show_hand(self):
        for card in self.hand:
            card.print_card()