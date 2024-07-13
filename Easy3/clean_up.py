'''
Given a string that consists of some words and an assortment of non-alphabetic characters, write 
a function that returns that string with all of the non-alphabetic characters replaced by 
spaces. If one or more non-alphabetic characters occur in a row, you should only have one space 
in the result (i.e., the result string should never have consecutive spaces).
'''

str_ = "---what's my +*& line?"

def clean_up(string): 
	cleaned = ''

	for char in string: 
		if char.isalpha(): 
			cleaned += char
		else: 
			cleaned += ' '
	
	cleaned = ' '.join(cleaned.split()) 
		
	return cleaned 

print(clean_up(str_))
