# >>>>> Tuples <<<<<
# Tuple is an immutable ( It allows duplicate values )
# Create tuple in literal way (direct assignment)
tuple_numbers = (2, 5, 3)
print(tuple_numbers[1])

# Create tuple using constructor
tuple_num = tuple([1, 2, 5])  # From list
tuple_num2 = tuple((1, 2, 5))  # From tuple
tuple_num3 = tuple({1, 2, 5})  # From set
print(tuple_num, tuple_num2, tuple_num3)

# This line leads to an error => TypeError: 'tuple' object does not support item assignment
# Can't change any value in the tuple because it is immutable
tuple_numbers[0] = 23

# Tuple have one value should have trailing comma
tuple_2 = ('a',)
print(tuple_2)

# Length of Tuple
print(len(tuple_numbers), len(tuple_2))

# Can't delete the element in the tuple
# Below line will result in error => TypeError: 'tuple' object doesn't support item deletion
del tuple_2[0]

# Delete the tuple
del tuple_2
''' 
The below print leads to error => NameError: name 'tuple_2' is not defined.
Because we deleted the tuple_2 in the above line
'''
print(tuple_2)
