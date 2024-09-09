'''
Build a program that randomly generates and prints Teddy's age. To get the age, you 
should generate a random number between 20 and 100, inclusive.
'''
import random

age = random.randint(20, 101)
name = input("Enter name: ") or "Teddy" 

print(f'{name} is {age} years old!')  
