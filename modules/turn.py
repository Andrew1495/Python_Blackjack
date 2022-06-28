
def draw_phase(deck,player_one,player_computer):
    if player_one.hand == [] and player_computer.hand == []:
        player_one.draw()
        player_computer.draw()
        player_one.draw()
        player_computer.draw()