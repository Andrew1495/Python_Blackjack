def hand_value(hand,has_ace):
    total = 0
    if ace_in_hand == False:
        for card in hand:
            total += card["value"]
            return total
    elif ace_in_hand == True:
        for card in hand:
            total += card["value"]
        if total > 21:
            total -= 10
        return total

    return total

def does_hand_ace(hand):
    for card in hand:
        if card["name"] == "Ace of Spades" or card["name"] == "Ace of Clubs" or card["name"] == "Ace of Diamonds" or card["name"] == "Ace of Hearts":
            return True
        else:
            return False


