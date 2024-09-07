"""Mortgage Calculator Module"""

def prompt(message):
    #define user prompts
    print(f'===> {message}')

def invalid_number(num_str):
    #define invalid input
    try:
        number = float(num_str)
        if number <= 0:
            raise ValueError(f'Value must be greater than 0: {num_str}')
    except ValueError:
        return True

    return False

#program begins...
prompt('Welcome to the Mortgage Calculator')
prompt('----------------------------------')

#to repeat the program after the calculation
while True:
    #loan amount
    prompt("For what amount is the loan?")
    loan_amount = input()
    #for invalid input
    while invalid_number(loan_amount):
        prompt("Must be a positive number")
        loan_amount = input()

    #interest rate
    prompt("What is the interest rate?")
    prompt("Example: 5 for %5, 2.5 for %2.5, etc..")
    apr = input()
    #for invalid input
    while invalid_number(apr):
        prompt("Interest rate must be a positive number")
        apr = input()

    #loan duration
    prompt("What is the duration of the loan (in years)?")
    loan_years = input()
    #for invalid input
    while invalid_number(loan_years):
        prompt("loan duration must be a positive number")
        loan_years = input()

    #converted infos
    annual_interest_rate = float(apr) / 100
    monthly_interest_rate = annual_interest_rate / 12
    months = float(loan_years) * 12
    loan_amount = float(loan_amount)

    #calculation
    monthly_payment = loan_amount * (
        monthly_interest_rate / (1 -(1 + monthly_interest_rate) ** (-months))
    )

    #returned output
    prompt(f"Your monthly payment is: ${round(monthly_payment, 2)}")

    #option to calculate again
    prompt("Would you like to calculate another payment? Y/N")
    answer = input().lower()

    while True:
        if answer.startswith("y") or answer.startswith("n"):
            break

        prompt("Please enter 'Y' or 'N':")
        answer = input().lower()

        if answer == 'n':
            break
