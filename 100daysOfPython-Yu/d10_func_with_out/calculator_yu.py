"""
This version is following Yu's instructions, so the result will look different
"""

#Add
def addition(n1, n2):
    return n1 + n2

#Subtract
def subtraction(n1, n2):
    return n1 - n2

#Multiply
def multiplication(n1, n2):
    return n1 * n2
#Divide
def division(n1, n2):
    return n1 / n2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,  
}
#get input from user here
num1 = int(input("What is the first number?: "))

for key in operations:
    print(key)
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What is your second number?: "))

#call operation
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

#print result to screen
print(f"{num1} {operation_symbol} {num2} = {answer}")