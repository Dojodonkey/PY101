'''
Create a function that takes 2 arguments, a list and a dictionary. The list will 
contain 2 or more elements that, when joined with spaces, will produce a person's 
name. The dictionary will contain two keys, "title" and "occupation", and the 
appropriate values. Your function should return a greeting that uses the person's 
full name, and mentions the person's title.
'''

name = input("Full Name: ") 
title_ = input("Title: ")
occupation_ = input("Occupation: ")

occ_dict = {"title" : title_ , "occupation" : occupation_} 
name_list = name.split()

def welcome(name, dictionary):
	name_ = str(name) 
	print(f'Hello {name_}! Nice to have a {occ_dict["title"]} {occ_dict["occupation"]} around.') 

welcome(name, occ_dict) 
