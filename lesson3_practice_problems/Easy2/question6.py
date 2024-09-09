#Back in the stone age (before CSS), we used spaces to align things on the screen.
#  If we have a 40-character wide table of Flintstone family members,
# how can we center the following title above the table with spaces?

title = "Flintstone Family Members"

def spaced_center(string):
    table = 40
    title_len = len(title)
    space = ' '
    space_per_side = space * int((table - title_len) / 2)
    return space_per_side + title + space_per_side

print(spaced_center(title))

#using built-in center function:
centered_title = title.center(40)
print(centered_title)