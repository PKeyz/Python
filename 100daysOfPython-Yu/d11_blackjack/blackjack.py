"""
First ideas:

Rules:
deck of cards -> shuffle
give card to player + card to dealer
10,K,Q = value 10
numbers = number_value

def check_sum(card_value):
    if previous_answer + card_value <= 21:
        print("Player wins!")

    else:
        print("Dealer wins!")

if hit_button:
    get new card from deck
    count new check_sum


if hand > 21 --> bust (loose instantly)

ace value 11 || 1

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
"""



