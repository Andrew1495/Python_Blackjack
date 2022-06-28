class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.take_one())

    def show_hand(self):
        for card in self.hand:
            card.print_card()

    def hand_total(self):
        sum = 0
        for card in self.hand:
            sum += card.card_value()
        print(sum)

    
