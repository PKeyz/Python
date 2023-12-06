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