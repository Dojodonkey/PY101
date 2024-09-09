#==> Check the strings seperately for Dino
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def name_check(string, name):
    if name in string:
        return True
    else:
        return False

print(name_check(str1, "Dino"))
print(name_check(str2, "Dino"))

#better solution
print('Dino' in str1)
print('Dino' in str2)