'''
Write a function that determines the mean (average) of the three scores passed to it, and 
returns the letter associated with that grade.

Numerical score letter grade list:

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'
Tested values are all between 0 and 100. There is no need to check for negative values or values 
greater than 100.
'''
score1 = int(input("Score 1: ")) 
score2 = int(input("Score 2: ")) 
score3 = int(input("Score 3: "))

def get_grade(sc1, sc2, sc3): 
	avg_score = (sc1 + sc2 + sc3) // 3 

	if 90 <= avg_score <= 100: 
		return 'A'
	elif 80 <= avg_score < 90: 
		return 'B' 
	elif 70 <= avg_score < 80: 
		return 'C' 
	elif 60 <= avg_score < 70: 
		return 'D'
	else: 
		return 'F' 

print(get_grade(score1, score2, score3))
