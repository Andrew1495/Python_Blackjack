def hand_value(hand,has_ace):
    total = 0
    for card in hand:
        total += card["value"]
        return total

    return total

def does_hand_ace(hand):
    for card in hand:
        if card["name"] == "Ace of Spades" or card["name"] == "Ace of Clubs" or card["name"] == "Ace of Diamonds" or card["name"] == "Ace of Hearts":
            return True
        else:
            return False


