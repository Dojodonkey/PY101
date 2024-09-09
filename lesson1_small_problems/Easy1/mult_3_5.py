'''
Write a function that computes the sum of all numbers between 1 and some other 
number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number 
is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).
'''
number = int(input("Number: "))

def multisum(number):
	multiples = []
	for i in range(1, number + 1): 
		if i % 3 == 0 or i % 5 == 0: 
			multiples.append(i) 
	print(sum(multiples))

multisum(number) 
