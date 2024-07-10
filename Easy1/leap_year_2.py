'''
In the previous exercise, we assumed that the Gregorian calendar has been in 
continuous use since the year 1. However, the Gregorian calendar wasn't adopted until 
much later; prior to that, much of the world used the Julian calendar, which observed 
leap year every 4 years.

in 1752, England, Ireland, and the British colonies all switched to the Gregorian 
calendar. Update the function from the previous exercise so it uses the Julian 
calendar prior to 1752, and the Gregorian calendar starting in 1752.
'''
year = int(input("Year: "))

def leap_years(year):
	if year <= 1752: 
		if year % 4 == 0: 
			print("True") 
		else: 
			print("False") 
	elif year % 400 == 0: 
		print("True") 
	elif year % 100 == 0: 
		print("False")
	elif year % 4 == 0: 
		print("True") 
	else: 
		print("False") 

leap_years(year) 
