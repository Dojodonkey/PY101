munsters_description = "The Munsters are creepy and spooky."
#==> "tHE mUNSTERS ARE CREEPY AND SPOOKY."

def reverse_case(string):
    result = ''
    for letter in string:
        if letter == letter.upper():
            result += letter.lower()
        elif letter == letter.lower():
            result += letter.upper()
        else:
            result += letter

    print(result)

reverse_case(munsters_description)

#or a more simple solution
print(munsters_description.swapcase())
