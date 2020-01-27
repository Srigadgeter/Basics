# >>>>> Dictionaries <<<<<
# Dictionary is a collection which unordered, indexed & changeable with no duplicates.
person = {
    'name': 'Gamer',
    'age': 22,
    'is_married': False
}

# Create dictionary using constructor
person2 = dict(firs_name='Sri', last_name='Gadgeter', age=22)
person3 = dict([('name', 'Gadgeter'), ('age', 23), ('is_married', True)])  # From list of tuples
print(person2, person3)

# Access value by the key
print(person['age'])
# print(person['dob'])  # It will throw an KeyError if the key doesn't exist in the given dictionary
print(person.get('name'))
print(person.get('father_name'))  # It will print 'None' if the key doesn't exist in the given dictionary
person['name'] = 'Gadgeter'  # update existing key
person['dob'] = 'dd-mm-yyyy'  # add a new key
print(person.get('name'), person.get('dob'))

# Provide default value
print(person.get('father_name', 'GamerFather'))  # We can show a default value for non-existing key
print(person)

# Get all keys from the dictionary
print(person.keys())

# Get all values from the dictionary
print(person.values())

# Get all key-value pairs from the dictionary
print(person.items())

# Make a copy
person_copy = person.copy()
print('person_copy >>>', person_copy)

# Delete a key-value pair using key & del option
del(person_copy['age'])
print(person_copy)

# Delete the dictionary
# del person_copy  # Uncomment this line and check the deletion of dictionary
print(person_copy)  # This results in error => NameError: name 'person_copy' is not defined

# Remove a key-value pair using key & pop function
person_copy.pop('name')
print(person_copy)

# Length of the dictionary
print(len(person_copy))

# Clear the dictionary
person_copy.clear()
print(person_copy)

# List of dictionary
people = [person, person3]
print(people)
print(people[0]['name'], people[1]['name'])
# =========================================
# Dictionary Game
numbers_in_words = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
}
phone_number = input('Phone Number please: ')
phone_number_in_words = ''
for number in phone_number:
    phone_number_in_words += f'{numbers_in_words[int(number)]} '
print(phone_number_in_words)
