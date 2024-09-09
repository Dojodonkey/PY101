"""Rock Paper Scissors Lizard Spock Module"""
import random

# Constants
VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
WINNING_COMBINATIONS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}

def prompt(message):
    """Display a formatted prompt message."""
    print(f'==> {message}')

def display_choices(user, computer):
    """Display the choices made by the user and computer."""
    prompt(f'You chose: {user}, computer chose: {computer}')

def determine_winner(user, computer):
    """Determine the winner of a round."""
    if user == computer:
        return "It's a tie"
    if computer in WINNING_COMBINATIONS[user]:
        return 'You win!'
    return 'Computer wins!'

def update_score(user_choice, comp_choice, scores):
    """Update the score based on the round result."""
    result = determine_winner(user_choice, comp_choice)
    if result == 'You win!':
        scores['user'] += 1
    elif result == 'Computer wins!':
        scores['computer'] += 1
    prompt(f"Score - You: {scores['user']}, Computer: {scores['computer']}")
    return result

def is_game_over(scores):
    """Check if the game is over."""
    if scores['user'] == 3:
        prompt("You win the game!")
        return True
    if scores['computer'] == 3:
        prompt("Computer wins the game!")
        return True
    return False

def play_again():
    """Ask if the player wants to play again."""
    while True:
        prompt('Play again? Y/N')
        answer = input().lower()
        if answer.startswith('y'):
            return True
        if answer.startswith('n'):
            return False
        prompt("That's not a valid answer")

def main():
    """Main game loop."""
    while True:
        scores = {'user': 0, 'computer': 0}

        while not is_game_over(scores):
            prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
            choice = input().lower()

            while choice not in VALID_CHOICES:
                prompt('That\'s not a valid input')
                choice = input().lower()

            computer_choice = random.choice(VALID_CHOICES)

            display_choices(choice, computer_choice)

            round_result = update_score(choice, computer_choice, scores)
            prompt(round_result)

            if not is_game_over(scores):
                prompt("Next round!")
                prompt("-----------------")

        if not play_again():
            break

    prompt('Thanks for playing!')

if __name__ == "__main__":
    main()
