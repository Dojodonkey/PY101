import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'MESSAGES' contains the contents of the JSON file as a Python dictionary or list

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(MESSAGES['welcome'])

prompt(MESSAGES['first'])
number1 = input()

while invalid_number(number1):
    prompt(MESSAGES['invalid number'])
    number1 = input()

prompt(MESSAGES["second"])
number2 = input()

while invalid_number(number2):
    prompt(MESSAGES['invalid number'])
    number2 = input()

prompt(MESSAGES['perform'])
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt(MESSAGES['invalid input'])
    operation = input()

match operation:
    case "1":
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) / int(number2)

prompt(f"The result is {output}")

while True:
    # ask for two numbers
    # ask for operation
    # perform operation and display results
    prompt(MESSAGES['again'])
    answer = input()
    if answer and answer[0].lower() != 'y':
        break