import random
import functions
#import numpy as np


"""
First ideas:

Rules:
deck of cards -> shuffle
10,K,Q = value 10
numbers = number_value
If you reach a Blackjack (21) your bet is multiplied by 3


if hand > 21 --> bust (loose instantly)

if hand_player == hand_dealer:
    draw

if hand_dealer < 17:
    must draw card

prints:

Do you want to play another game of blackjack? Type 'y' or 'n': 

The dealing of the cards in a game of Blackjack is as follows:

A card is dealt to the player facing upwards (visible to everyone).
The dealer deals a card to himself visible to everyone.
Another card is given to the player facing upwards.
The dealer deals a card facing downwards for himself.
The player has to decide whether to stand with the current set of cards or get another card.
If the player decides to hit, another card is dealt.
If the player decides to stand, then the dealer reveals his hidden card.
The dealer does not have the authority to decide whether to hit or stand. The general rule is that the dealer needs 
to keep hitting more cards if the sum of dealer’s cards is less than 17.

As soon as the sum of dealer’s cards is either 17 or more, the dealer is obliged to stand.
According to the final sum of the cards, the winner is decided.

"""

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
casino_bank = 0
#player_stake = 0
#create original deck
originalDeck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'Jack','Jack','Jack','Jack','Queen','Queen','Queen','Queen','King','King','King','King','Ace','Ace','Ace','Ace',]

player_hand = []
dealer_hand = []

player_points = 0
dealer_points = 0
dealer_points_visible = 0

player_turn = 0
dealer_turn = 0



class BlackJack:
    

    start_game = input('Print any key to start the game, print "no" to quit the game\n')
    game_play = True
    
    while game_play:
        global player_bank
        global casino_bank
        global player_hand
        global dealer_hand
        global player_points
        global dealer_points
        
        
        if start_game == 'no':
            'You quit the game.'

        else:
            print(logo)
            startGameScreen = print (f"You start with {player_bank} $")
            # deck of cards -> shuffle
            shuffled_deck = random.sample(originalDeck, len(originalDeck))
            
            #set up a new bet and update local variables in-game
            new_values = functions.player_stake(player_bank, casino_bank)
            player_bank = new_values[0]
            casino_bank = new_values[1]
            
            initial_deal_hand_arr = functions.deal_hand(shuffled_deck,4)
            player_hand.append(initial_deal_hand_arr[0])
            player_hand.append(initial_deal_hand_arr[2])
            dealer_hand.append(initial_deal_hand_arr[1])
            dealer_hand.append(initial_deal_hand_arr[3])
            
            shuffled_deck = functions.update_deck(shuffled_deck, 4)
            player_points = functions.count_points(player_hand, player_points)
            dealer_points = functions.count_points(dealer_hand, dealer_points)
            print(f'Your starting hand contains {player_hand} and you have {player_points} points')
            print(f'Dealers open card is [{dealer_hand[1]}] and he has {dealer_points} points')
            
            while (player_points <= 21) or (dealer_points <= 21):
                
            
                input = ('Would you like to "Hit" or "Stand" ?')
                if input == 'Hit':
                    player_hand = functions.deal_hand(shuffled_deck, 1)
                    shuffled_deck = functions.update_deck(shuffled_deck,1)
                    print(f'Your starting hand contains {player_hand} and you have {player_points} points')
                
                    #dealers turn
                    print('Dealers card value is under 17. Dealer "hits"')
                    if(dealer_points < 17):
                        dealer_hand = functions.deal_hand(shuffled_deck,1)
                        shuffled_deck = functions.update_deck(shuffled_deck,1)
                        print(f'Dealers open cards are [{dealer_hand}] and he has {dealer_points} points')
                    else:
                