"""Rock Paper Scissors Module"""
import random

#constant
VALID_CHOICE = ['rock', 'paper', 'scissors']

#function for prompts
def prompt(message):
    print(f'==> {message}')

#function for output user & computer choices
def choices_display(user, computer):
    prompt(f'You chose: {choice}, computer chose: {computer_choice}')

    #conditions for user win
    if ((choice == 'rock' and computer_choice == 'scissors') or
        (choice == 'scissors' and computer_choice == 'paper') or
        (choice == 'paper' and computer_choice == 'rock')):
        prompt('You win!')
    #conditions for computer win
    elif ((computer_choice == 'rock' and choice == 'scissors') or
        (computer_choice == 'scissors' and choice == 'paper') or
        (computer_choice == 'paper' and choice == 'rock')):
        prompt('Computer wins!')
    #case of tie
    else:
        prompt("It's a tie")

#while True for game repition
while True:
    #user input
    prompt(f'Choose one: {', '.join(VALID_CHOICE)}')
    choice = input()

    #invalid user input
    while choice not in VALID_CHOICE:
        prompt('Thats not a valid input')
        choice = input()

    #computer input
    computer_choice = random.choice(VALID_CHOICE)

    #call choices display
    choices_display(choice, computer_choice)

    #play again option
    while True:
        prompt('Play again? Y/N')
        y_n = input().lower()

        if y_n.startswith('y') or y_n.startswith('n'):
            break
        else:
            prompt("That's not a valid answer")
            prompt('Play again? Y/N')

    if y_n[0] == 'n':
        break
