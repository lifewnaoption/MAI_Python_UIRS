vict = {
    'scissors': ['lizard', 'paper'],
    'paper': ['spock', 'rock'],
    'rock': ['lizard', 'scissors'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}

def rpsls(pl1, pl2):
    pl1 = pl1.lower()
    pl2 = pl2.lower()

    if vict[pl2] == vict[pl1]:
        return('Draw!')
        
    if pl2 in vict.get(pl1):
        return('Player 1 Won!')

    if pl2 not in vict.get(pl1):
        return('Player 2 Won!')
        
rpsls('paper', 'rock')
