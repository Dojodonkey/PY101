"""
Calculator Module
"""
# Ask user for two numbers (num1 & num2)
# Ask user for an operation to perform
# Perform operation and print the result to the terminal

def prompt(message):
    print(f'==> {message}')

def invalid_num(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def calculator():
    prompt('Welcome to Calculator!')

    prompt("What's the first number?")
    num1 = input()

    while invalid_num(num1):
        prompt("Hmm... that doesn't look like a valid number.")
        num1 = input()

    prompt("What's the second number?")
    num2 = input()

    while invalid_num(num2):
        prompt("Hmm... that doesn't look like a valid number.")
        num2 = input()

    prompt("What operation would you like to perform?\n1. Add\n2. Subtract\n"
    "3. Multiply\n4. Divide")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()

    num1 = float(num1)
    num2 = float(num2)

    match operation:
        case '1':
            output = num1 + num2
        case '2':
            output = num1 - num2
        case '3':
            output = num1 * num2
        case '4':
            output = num1 / num2

    print(f"==> Result: {output}")

#Main loop
while True:
    calculator()
    prompt("Would you like to perform another calculation? (Y/N)")
    response = input().strip().lower()
    if response != 'y':
        break
