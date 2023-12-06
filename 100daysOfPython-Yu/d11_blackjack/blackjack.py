import random
import functions

"""
First ideas:

Rules:
deck of cards -> shuffle
10,K,Q = value 10
numbers = number_value


Next task : dealing initial hand->> 
give card to player + card to dealer + card to player + card to dealer [open] 

def check_sum(card_value):
    if previous_answer + card_value <= 21:
        print("Player wins!")

    else:
        print("Dealer wins!")

if hit_button:
    get new card from deck
    count new check_sum


if hand > 21 --> bust (loose instantly)

ace value 1 || 11 if hand = 0 ace=11, elif hand+ 11 < 21 hand = hand +11 else ace=1 => hand + 1

player get's their cards first, if hand > 21 bust instantly *(loose first too)

if hand_player == hand_dealer:
    draw

if hand_dealer < 17:
    must draw card

cards are list = []
ace represented as 11

if hand_player || hand_dealer contains 11 and hand > 21:
    get ace position in hand
    hand[x] = 1
    hand_value -= 10


prints:

Your Cards[9,10]
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: 
Your  final hand: [9,10]
Computer's final hand: [8,10]
You Win
Do you want to play a game of blackjack? Type 'y' or 'n': 

in python do while done with do block - and recursion inside loop

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
player_bank = 400
casino_bank = 0
#player_stake = 0
#create original deck
originalDeck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'Jack','Jack','Jack','Jack','Queen','Queen','Queen','Queen','King','King','King','King','Ace','Ace','Ace','Ace',]


class BlackJack:
    

    start_game = input('Print any key to start the game, print "no" to quit the game\n')

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
    
    

    """_summary_
    #give card to player + card to dealer
    player_hand = []
    dealer_hand = []

    player_hand.append(shuffled_deck[0])
    dealer_hand.append(shuffled_deck[1])


    print(shuffled_deck)
    print(player_hand)
    print(dealer_hand)
    """



