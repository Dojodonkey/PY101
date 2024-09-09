'''
Write a function that takes two strings as arguments, determines the length of the 
two strings, and then returns the result of concatenating the shorter string, the 
longer string, and the shorter string once again. You may assume that the strings are 
of different lengths.
'''
arg1 = input("1st argument: ")  
arg2 = input("2nd argument: ")

def short_long_short(arg1, arg2): 
	if len(arg1) > len(arg2): 
		long = arg1
		short = arg2 
	else: 
		long = arg2
		short = arg1
	print(short + long + short) 

short_long_short(arg1, arg2)
