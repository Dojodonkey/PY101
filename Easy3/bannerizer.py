'''
Write a function that takes a short line of text and prints it within a box.
'''

txt = input("Write a one-liner: ") 

def print_in_box(txt): 
	width = len(txt) + 4 

	print('+' + '-' * width + '+') 

	print('|' + ' ' * width + '|')

	print('|' + ' ' * 2 + txt + ' ' * 2 + '|')

	print('|' + ' ' * width + '|') 

	print('+' + '-' * width + '+') 

print_in_box(txt) 
