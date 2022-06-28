class Card:
    def __init__(self, suit):
        self.suit = suit
        self.value = {
            "name": "",
            "value": 0
        }

    def print_card(self):
        icon =""
        if self.suit == "hearts":
            icon = "♥"
            print(f"{self.value['name']}{icon}")
        elif self.suit == "clubs":
            icon = "♣"
            print(f"{self.value['name']}{icon}")
        elif self.suit == "spades":
            icon = "♠"
            print(f"{self.value['name']}{icon}")
        elif self.suit == "diamonds":
            icon = "♦"
            print(f"{self.value['name']}{icon}")
