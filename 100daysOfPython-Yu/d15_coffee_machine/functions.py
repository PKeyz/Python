import constants


# TODO: 1. 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

def prompt_user_drink():
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    return drink_choice


# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
def turn_machine_off():
    turn_off = input("Would you like to turn down the coffe machine? Print 'yes' to turn down")
    if turn_off == 'yes':
        is_turned_on = False


# TODO: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def print_report():
    report_input = input('Would you like to see the machine report? Press "y" or "n".')
    if report_input == 'report':
        print(
            f'Water: {constants.water}ml\nMilk: {constants.milk}ml\nCoffee: {constants.coffee}ml\n Money: ${constants.money}')


# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def resources_sufficient(drink_choice: str):
    is_brewable = False
    if drink_choice == 'espresso':
        if constants.water < constants.drink_dict[0].get('water'):
            print('Sorry there is not enough water.')
        elif constants.coffee < constants.drink_dict[0].get('coffee'):
            print('Sorry there is not enough coffee.')
        else:
            is_brewable = True
            return is_brewable
    elif drink_choice == 'latte':
        if constants.water < constants.drink_dict[1].get("water"):
            print('Sorry there is not enough water.')
        elif constants.coffee < constants.drink_dict[1].get('coffee'):
            print('Sorry there is not enough coffee.')
        elif constants.milk >= constants.drink_dict[1].get('milk'):
            print('Sorry there is not enough milk.')
        else:
            is_brewable = True
            return is_brewable
    elif drink_choice == 'cappuccino':
        if constants.water < constants.drink_dict[2].get('water'):
            print('Sorry there is not enough water.')
        elif constants.coffee < constants.drink_dict[2].get('coffee'):
            print('Sorry there is not enough coffee.')
        elif constants.milk >= constants.drink_dict[2].get('milk'):
            print('Sorry there is not enough milk.')
        else:
            is_brewable = True
            return is_brewable


# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def count_money():
    quarters = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01

    amount_quarters = int(input('Insert the amount of quarters.'))
    amount_dimes = int(input('Insert the amount of dimes.'))
    amount_nickles = int(input('Insert the amount of nickels.'))
    amount_pennies = int(input('Insert the amount of pennies.'))

    amount_total = ((quarters * amount_quarters) + (dimes * amount_dimes) + (
            nickles * amount_nickles) + pennies * amount_pennies)

    return amount_total


# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

def check_transaction_success(amount_total: int, drink_choice: str):
    is_transaction_successful = False
    if (drink_choice == 'espresso') and (amount_total >= constants.drink_dict[0].get("price")):
        constants.money += constants.drink_dict[0].get("price")
        print(f'Here is ${amount_total - constants.drink_dict[0].get("price")} in change')
        is_transaction_successful = True
        return is_transaction_successful
    elif (drink_choice == 'latte') and (amount_total >= constants.drink_dict[1].get("price")):
        constants.money += constants.drink_dict[1].get("price")
        print(f'Here is ${amount_total - constants.drink_dict[1].get("price")} in change')
        is_transaction_successful = True
        return is_transaction_successful
    elif (drink_choice == 'cappuccino') and (amount_total >= constants.drink_dict[2].get("price")):
        constants.money += constants.drink_dict[2].get("price")
        print(f'Here is ${amount_total - constants.drink_dict[2].get("price")} in change')
        is_transaction_successful = True
        return is_transaction_successful
    else:
        print(f'Sorry that\'s not enough money. ${amount_total} refunded.')


# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.

def make_coffe(is_brewable: bool, is_transaction_successful: bool, drink_choice):
    if is_brewable and is_transaction_successful:
        print_report()
        if drink_choice == 'espresso':
            constants.water - constants.drink_dict[0].get("water")
            constants.coffee - constants.drink_dict[0].get("coffee")
            constants.milk - constants.drink_dict[0].get("milk")
            print('Making an Espresso, have a nice break!')
        elif drink_choice == 'latte':
            constants.water - constants.drink_dict[1].get("water")
            constants.coffee - constants.drink_dict[1].get("coffee")
            constants.milk - constants.drink_dict[1].get("milk")
            print('Making a Latte, have a nice break!')
        elif drink_choice == 'cappuccino':
            constants.water - constants.drink_dict[2].get("water")
            constants.coffee - constants.drink_dict[2].get("coffee")
            constants.milk - constants.drink_dict[2].get("milk")
            print('Making a Cappuccino, have a nice break!')
        print_report()


# TODO 8. Refill machine
def refill():
    resource_choice = input('What would you like to refill? Choose between: water/coffee/milk/money')
    refill_amount = input('How much would you like to refill? Numbers in ml or $')

    if resource_choice == 'water':
        constants.water += refill_amount
    elif resource_choice == 'coffee':
        constants.coffee += refill_amount
    elif resource_choice == 'milk':
        constants.milk += refill_amount
    elif resource_choice == 'money':
        constants.money += refill_amount
