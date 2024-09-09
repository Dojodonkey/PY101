#Given a list of numbers [1, 2, 3, 4, 5],
# mutate the list by removing the number at index 2, so that the list becomes [1, 2, 4, 5].

numbers = [1, 2, 3, 4, 5]
numbers.remove(numbers[2])
#remove() searches for first instance and deletes it
print(numbers)

#or
del numbers[2]
#del accesses list directly to delete the element of that index
print(numbers)
#deletes index 2 again