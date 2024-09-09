length =int(input("Room Length: ")) 
width = int(input("Room Width: ")) 
feet_or_meters = input("In feet or meters? ") 

square_m = length * width 
square_f = (length * width) * 10.7639 

if feet_or_meters == 'meters': 
	print(f"square meters: {square_m}") 
else:
	print(f"square feet: {square_f}") 

