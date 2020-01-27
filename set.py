# >>>>> Sets <<<<<
# Set is a unordered & non-indexed collection of unique elements

# Create set using constructor
uniques = set([1, 12, 33, 3, 23, 33, 44])  # From list
uniques2 = set((1, 12, 33, 3, 23, 33, 44))  # From tuple
print(uniques, uniques2)

set1 = {3, 5, 1}
# Add an item to the set
set1.add(4)
set1.add(3)  # The number 3 is already present. So it wont add
print('>>>', set1)

# Remove an item from the set
set1.remove(5)  # Remove an item by value
print(set1)

# Clear the set
# set1.clear()
print(set1)

# Delete the set
# del set1
print(set1)  # Will result in error => NameError: name 'set1' is not defined

# union of two sets
union = uniques | set1
print('union >>>', union)

# intersection of two sets
intersection = uniques & set1
print('intersection >>>', intersection)

# element presents in either first or second & not both of two sets
not_both = uniques ^ set1
print('not_both >>>', not_both)

# difference of two sets
difference1 = uniques - set1
difference2 = set1 - uniques
print('diff >>>', difference1, difference2)
