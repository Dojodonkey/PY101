#Write two different ways to remove all of the elements from the following list:
#first way to clear list
numbers = [1, 2, 3, 4]
#using clear function
numbers.clear()
print(numbers)

#for the second way to clear the list
numbers2 = [1, 2, 3, 4]
#using a while loop (a non-empty list is True, an empty list is False)
while numbers2:
    numbers2.pop()
print(numbers2)
