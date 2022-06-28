class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_card(self):
        icon =""
        if self.suit == "hearts":
            icon = "♥"
            print(f"{self.value}{icon}")
        elif self.suit == "clubs":
            icon = "♣"
            print(f"{self.value}{icon}")
        elif self.suit == "spades":
            icon = "♠"
            print(f"{self.value}{icon}")
        elif self.suit == "diamonds":
            icon = "♦"
            print(f"{self.value}{icon}")
