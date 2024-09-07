"""Rock Paper Scissors Module"""
import random

# Constants
VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

# Function for prompts
def prompt(message):
    print(f'==> {message}')

# Function for output user & computer choices
def choices_display(user, computer):
    prompt(f'You chose: {user}, computer chose: {computer}')

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie"
    elif ((user == 'rock' and computer in ['scissors', 'lizard']) or
          (user == 'paper' and computer in ['rock', 'spock']) or
          (user == 'scissors' and computer in ['paper', 'lizard']) or
          (user == 'lizard' and computer in ['paper', 'spock']) or
          (user == 'spock' and computer in ['rock', 'scissors'])):
        return 'You win!'
    else:
        return 'Computer wins!'

# Main game loop
while True:
    # User input
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().lower()

    # Invalid user input
    while choice not in VALID_CHOICES:
        prompt('That\'s not a valid input')
        choice = input().lower()

    # Computer input
    computer_choice = random.choice(VALID_CHOICES)

    # Display choices
    choices_display(choice, computer_choice)

    # Determine and display winner
    result = determine_winner(choice, computer_choice)
    prompt(result)

    # Play again option
    while True:
        prompt('Play again? Y/N')
        y_n = input().lower()

        if y_n.startswith('y') or y_n.startswith('n'):
            break
        else:
            prompt("That's not a valid answer")

    if y_n.startswith('n'):
        break

prompt('Thanks for playing!')
