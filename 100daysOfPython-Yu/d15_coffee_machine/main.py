import functions

is_turned_on = True

while is_turned_on:
    user_drink = functions.prompt_user_drink()

    functions.resources_sufficient(user_drink)

    #user_payment = functions.count_money()

    #functions.check_transaction_success(user_payment, user_drink)

