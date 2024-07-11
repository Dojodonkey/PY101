'''
Write a function that takes a non-empty string argument and returns the middle character(s) of 
the string. If the string has an odd length, you should return exactly one character. If the 
string has an even length, you should return exactly two characters.
'''

strng = input("Enter a string: ")

def center_of(strng): 
	str_len = len(strng) 
	result = [] 
	if str_len % 2 == 0: 
		result.append(strng[str_len // 2 - 1]) 
		result.append(strng[str_len // 2]) 
		return ''.join(result) 
	else: 
		return strng[str_len // 2]  

print(center_of(strng))
