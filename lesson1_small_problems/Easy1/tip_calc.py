bill = int(input("Check: ")) 
tip_perc = int(input("Tip Percent: ")) 

def tip_calculator(bill, tip_perc): 
	print(bill + (bill * (tip_perc / 100)))

tip_calculator(bill, tip_perc) 


 

