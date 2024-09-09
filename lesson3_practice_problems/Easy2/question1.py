numbers = [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1] without mutating original list (2 methods)

print(numbers[::-1])
print(list(reversed(numbers)))