'''
Write a function that takes a year as input and returns the century. The return value should be 
a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as 
appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th 
century.
'''

year = int(input("Year: "))

def century(year): 
    year_str = str(year)    #year(int) turned into a string 
    century_ = 0             #century initialized
    
    if len(year_str) <= 2: 
        century_ = 1  
    elif len(year_str) == 3: 
        century_ = int(year_str[0]) + 1 
    elif len(year_str) == 4:
        century_ = int(year_str[0] + year_str[1]) + 1
    elif len(year_str) == 5:    
        century_ = int(year_str[0] + year_str[1] + year_str[2]) + 1
    
    cent_str = str(century_)    #century(int) turned into a string
    
    if cent_str[-1] == '1': 
        return cent_str + 'st' 
    elif cent_str[-1] == '2': 
        return cent_str + 'nd'
    elif cent_str[-1] == '3': 
        return cent_str + 'rd'
    else: 
        return cent_str + 'th' 

print(century(year))
