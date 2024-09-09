'''
Write a function that takes a string argument and returns a new string that contains the value 
of the original string with all consecutive duplicate characters collapsed into a single 
character.
'''

strng = input("string = ") 

def crunch(strng): 
	result = strng[0]
	for i in range(1, len(strng)): 
		if strng[i] != strng[i - 1]: 
			result += strng[i]
	return result 

print(crunch(strng))


