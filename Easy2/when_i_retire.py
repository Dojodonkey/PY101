'''
Build a program that displays when the user will retire and how many years she has to work till 
retirement.
'''
from datetime import date

age = int(input("What is your age? ")) 
ret_age = int(input("At what age would you like to retire? ")) 
diff_to_ret = ret_age - age

current_year = date.today().year

print(f"It's {current_year}. You will retire in {current_year + diff_to_ret}." 
	f" You have only {diff_to_ret} years of work to go!") 
