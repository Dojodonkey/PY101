'''
Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words.
'''

string_ = input("Write a string: ") 
pen_list = string_.split()

if len(pen_list) == 1 or len(pen_list) == 0: 
	print("bruh")
else:
	def penultimate(string): 
		print(pen_list[len(pen_list) - 2])


	def middle_string(string):
		print(pen_list[len(pen_list) // 2])

middle_string(string_) 
penultimate(string_)
	  

