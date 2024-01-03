import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
player_bank = 1000
casino_bank = 10000
#player_stake = 0
#create original deck
originalDeck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'Jack','Jack','Jack','Jack','Queen','Queen','Queen','Queen','King','King','King','King','Ace','Ace','Ace','Ace',]
# deck of cards -> shuffle
shuffled_deck = random.sample(originalDeck, len(originalDeck))

player_hand = []
dealer_hand = []
dealer_hand_visible = []

player_points = 0
dealer_points = 0
dealer_points_visible = 0

player_turn = 0
dealer_turn = 0

player_last_turn = True #True = hit False = stand
dealer_last_turn = True #True = hit False = stand

point_limit = 21

