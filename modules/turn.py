
def draw_phase(deck,player_one,player_computer):
    if player_one.hand == [] and player_computer.hand == []:
        player_one.draw()
        player_computer.draw()
        player_one.draw()
        player_computer.draw()


def has_ace(player):
    ace = False
    for card in player.hand:
        card.value["name"] == "Ace"
        ace = True
    return ace

def player_score(player,ace):
    score = 0
    if ace == True and hand_total() > 21:
        score = hand_total() - 10
    else:
        score = hand_total()
    return score

def stick_or_twist(player, deck):
    player_choice = ""
    if player_choice == "hit"  and player_choice != "stick":
        player.draw()


    