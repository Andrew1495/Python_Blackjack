def hand_value(hand,has_ace):
    total = 0
    if has_ace == False:
        for card in hand:
            total += card["value"]
        return total
    elif has_ace == True:
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




def compare_hands(player_hand_total, computer_hand_total):
    winner = None
    if player_hand_total >21:
        winner = "computer"
        return winner
    elif computer_hand_total > 21:
        winner = player
        return winner
    elif player_hand_total > computer_hand_total and player_hand_total <= 21:
        winner = "player"
        return winner
    elif player_hand_total < computer_hand_total and computer_hand_total <=21:
        winner = "computer"
        return winner
    elif player_hand_total == computer_hand_total:
        winner = "draw"
        return winner
    

