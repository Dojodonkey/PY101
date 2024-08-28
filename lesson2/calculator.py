"""A simple calculator with internationalization support."""

import json

def prompt(message):
    """Print a prompt message."""
    print(f"==> {message}")

def invalid_number(number_str):
    """Check if the input string is an invalid number."""
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang='pt'):
    """Retrieve a message from the language dictionary."""
    return MESSAGES[lang][message]

with open('calculator_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

print(messages('welcome'))

while True:
    while True:
        prompt(messages('first'))
        number1 = input()

        if not invalid_number(number1):
            break

        prompt(messages('invalid number'))

    while True:
        prompt(messages('second'))
        number2 = input()

        if not invalid_number(number2):
            break

        prompt(messages('invalid number'))

    while True:
        prompt(messages('perform'))
        operation = input()

        if operation in ["1", "2", "3", "4"]:
            break

        prompt(messages('invalid input'))

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    output = round(output, 2)  # Round the result to two decimals

    prompt(output)

    prompt(messages('again'))
    answer = input()
    if answer[0].lower() != 'y':
        break
