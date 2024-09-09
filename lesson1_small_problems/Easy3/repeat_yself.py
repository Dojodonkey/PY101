'''
Write a function that takes two arguments, a string and a positive integer, then prints the 
string as many times as the integer indicates.
'''

strng = input("Say something: ") 
rep = int(input("How many times? "))

def repeat(strng, rep): 
	for i in range(rep): 
		print(strng) 

repeat(strng, rep)
