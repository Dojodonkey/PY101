'''
Write a function that takes one argument, a positive integer, and returns a string of 
alternating '1's and '0's, always starting with a '1'. The length of the string should match the 
given integer.
'''

int_ = int(input("Write a number: ")) 

def stringy(number): 
	result = '1'

	for i in range(1, number): 
		if result[i - 1] == '1': 
			result += '0'
		else: 
			result += '1'
	return result 

print(stringy(int_))
