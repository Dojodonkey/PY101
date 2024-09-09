'''
Write a function that takes a number as an argument. If the argument is a positive number, return 
the negative of that number. If the argument is a negative number, return it as-is.
'''

num_ = int(input("Enter a number: ")) 

def negative(num_): 
	if num_ > 0:
		neg_num = - num_
		return neg_num
	else: 
		return num_ 

print(negative(num_))
