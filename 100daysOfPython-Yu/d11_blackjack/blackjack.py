import global_variables
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

1. check global_variables.dealer_cards_visible [1:] doesn't seem to work and shows only the second card
2.update player_bank when getting into a new round
3.null player hand when new round
4.reshuffle the deck when new
5. eventually move player_stake to global.neutral area and move to either casino, or player_bank after round.

"""

class BlackJack:
    

    start_game = input('Print any key to start the game, print "no" to quit the game\n')
    game_play = True
    
    while game_play:
        
        if start_game == 'no':
            'You quit the game.'

        else:
            print(global_variables.logo)
            startGameScreen = print (f"You start with {global_variables.player_bank} $")
            print(f'Dealer starts with {global_variables.casino_bank}')
            
            #set up a new bet and update local variables in-game
            new_values = functions.player_stake(global_variables.player_bank, global_variables.casino_bank)
            global_variables.player_bank = new_values[0]
            global_variables.casino_bank = new_values[1]
            
            initial_deal_hand_lst = functions.deal_hand(global_variables.shuffled_deck,4)
            global_variables.player_hand.append(initial_deal_hand_lst[0])
            global_variables.dealer_hand.append(initial_deal_hand_lst[1])
            global_variables.player_hand.append(initial_deal_hand_lst[2])
            global_variables.dealer_hand.append(initial_deal_hand_lst[3])
            global_variables.dealer_hand_visible = global_variables.dealer_hand[1:]
            shuffled_deck = functions.update_deck(global_variables.shuffled_deck, 4)
            
            #global_variables.player_points = 
            functions.count_points(global_variables.player_hand, global_variables.player_points)
            #global_variables.dealer_points = 
            functions.count_points(global_variables.dealer_hand, global_variables.dealer_points)
            
            print(f'Your starting hand contains {global_variables.player_hand} and you have {global_variables.player_points} points')
            print(f'Dealers open card is {global_variables.dealer_hand_visible} and he has {global_variables.dealer_points_visible} points')
            
            while (global_variables.player_points <= global_variables.player_bank):
                if((global_variables.player_points > global_variables.point_limit) or (global_variables.dealer_points == global_variables.point_limit)):
                    print('Bust! Dealer wins!')
                    print(f'Dealer\'s cards are {global_variables.dealer_hand} and dealer\'s points are {global_variables.dealer_points}')
                    functions.clean_values_rerun(False)
                    # global_variables.player_bank -= global_variables.casino_bank
                    # global_variables.dealer_bank += global_variables.casino_bank
                    break
                    #continue game?
                    break
                elif((global_variables.player_points == global_variables.point_limit) and (global_variables.dealer_points == global_variables.point_limit)):
                    print('Push!')
                    break
                    #continue game?
                elif((global_variables.player_points == global_variables.point_limit) and (global_variables.dealer_points < global_variables.point_limit)):
                    print('Win!')
                    break
                    #continue game?
                else:
                    functions.hit_or_stand()
            
                