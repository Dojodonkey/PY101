'''
Write a program that asks the user to enter an integer greater than 0, then asks 
whether the user wants to determine the sum or the product of all numbers between 1 
and the entered integer, inclusive.
'''
integer =int(input("Please enter an integer greater than 0: "))
s_p = input("Enter 's' to compute the sum, or 'p' to compute the product: ")
        
int_list = []

for i in range(1, integer + 1): 
	int_list.append(i)

if s_p == 's': 
	print(sum(int_list))
elif s_p == 'p': 
	product = 1
	for num in int_list: 
		product *= num
	print(product)
