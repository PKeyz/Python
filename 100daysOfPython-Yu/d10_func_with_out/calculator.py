

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

"""
What's the first Number?: INPUT
+-*/
Pick an operation: INPUT
What's the next number?: INPUT
3.0 * 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: INPUT
"""
def addition(a, b):
    """
    Taking two integers as inputs, adds them and returns a result value
    """
    result = a + b
    return result

def subtraction(a, b):
    """
    Taking two integers as inputs, subtracts them and returns a result value
    """
    result = a - b
    return result

def division(a, b):
    """
    Taking two integers as inputs, divides them and returns a result value
    """
    result = a / b
    return result

def multiplication(a, b):
    """
    Taking two integers as inputs, multiplies them and returns a result value
    """
    result = a * b
    return result

def ask_for_continuation(ask_to_continue):
    """
    Asks user input as string, if input is "y", returns is_continuing True, else False
    """
    if ask_to_continue == "y":
        is_continuing = True
        return is_continuing
    else:
        is_continuing = False
        return is_continuing
    
def calculate(a, b, operation):
    """
    Taking two integers and the operation string as inputs to calculate the result of the operation
    """
    if operation == "+":
        addition(a, b)
    elif operation == "-":
        subtraction(a, b)
    elif operation == "/":
        division(a, b)
    elif operation == "*":
        multiplication(a, b)
    else:
        print("Wrong operation selected, Try again\n")

is_continuing = True

while(is_continuing):
    
    a = input("What's the first number?: ")
    print("+\n-\n/\n*\n")
    operation = input("Pick an operation: ")
    b = input("What's the next number?: ")

    calculate(a, b, operation)



    print(f"")

    ask_to_continue = input("Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: ")
    ask_for_continuation(ask_to_continue)
    
