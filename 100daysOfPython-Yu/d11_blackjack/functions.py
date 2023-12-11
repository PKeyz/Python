new_values = []

def player_stake(player_bank,casino_bank):
    """promt the user to put an amount of money from playerBank into current game
        and reduce the amount of playerBank according to the choosen amount

    Args:
        player_bank (int): current amount of money in players bank
        casino_bank (int): current amount owned by casino
        
        Return: array with updated values for [player_bank, casino_bank]
    """
    global new_values
    valid_choice = True
    #current_balance = print(f'Your current balance is {player_bank}' + '$')
             
    while valid_choice:
        amount_choosen = input('What is your stake? Print: "1", "5","25", "50", "100", "500", "all in"\n')
    
        match amount_choosen:
            case "1":
                amount_choosen = 1
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case "5":
                amount_choosen = 5
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case "25":
                amount_choosen = 25
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case "50":
                amount_choosen = 50
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case "100":
                amount_choosen = 100
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case "500":
                amount_choosen = 500
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case "all in":
                amount_choosen = player_bank
                print(f"You chose to put {amount_choosen}" + "$ into this round")
                
        if (player_bank - amount_choosen) >= 0:
            player_bank -= amount_choosen
            casino_bank += amount_choosen
            
            current_balance = print(f'Your current balance is {player_bank}' + '$')
            valid_choice = False
            break
        elif (player_bank - amount_choosen) <= 0:
            print("You're betting too high! Please choose a new bet!")
    new_values = [player_bank,casino_bank]
    return new_values


def deal_hand(shuffled_deck, number:int):
    """deals the first hand of the game in order: card to player + card to dealer + card to player + card to dealer || equals to "hit" with number = 1
    @args: shuffled deck: arr
    player_hand: 0,1
    dealer_deck: 1,3
    """
    hand_dealt = shuffled_deck[0:number]
    return hand_dealt
    
def update_deck(shuffled_deck, number : int):
    """Def deletes the cards moved to player or dealer hand from deck

    Args:
        shuffled_deck (arr): full original shuffled deck of 52 cards
        number (int) : number of cards to remove from old arr
    Returns:
        arr: returns arr of new deck minus initially dealt cards 
    """
    updated_shuffled_deck = shuffled_deck[number:]
    return updated_shuffled_deck

def count_points(player_hand,player_points: int):
    player_value = 0
    for cards in player_hand:
        if cards in ['Jack', 'Queen', 'King']:
            player_value += 10
        elif cards == 'Ace':
            if (player_points + 11) <= 21:
                player_value += 11
            else:
                player_value += 1
        else:
            player_value += cards
    return player_value

#def stand():
    
    