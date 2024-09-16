dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
#because num_list references the original, it is also changed.

#if we wanted to add a new key and value to dictionary:
dictionary['second'] = [3, 4]
print(dictionary)