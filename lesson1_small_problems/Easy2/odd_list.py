'''
Write a function that returns a list that contains every other element of a list that 
is passed in as an argument. The values in the returned list should be those values 
that are in the 1st, 3rd, 5th, and so on elements of the argument list.
'''

def oddities(list): 
	odd_list = []
	for i in range(0, len(list), 2):
		odd_list.append(list[i])
	return odd_list 

#using slicing

def oddities(list): 
	odd_list = [list[0 : len(list) + 1 : 2]] 
	return odd_list
