'''
A double number is an even-length number whose left-side digits are exactly the same as its 
right-side digits. For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 
334433, and 107 are not.

Write a function that returns the number provided as an argument multiplied by two, unless the 
argument is a double number. If the argument is a double number, return the double number as-is.
'''

num_ = int(input("Write a number: ")) 

def twice(number): 
	num_str = str(number) 
	num_lst = list(num_str) 

	num1 = num_lst[:len(num_lst)//2] 
	num2 = num_lst[len(num_lst)//2:]

	if int(''.join(num1)) == int(''.join(num2)): 
		return number
	else: 
		return number * 2 

print(twice(num_))
