# >>>>> Strings <<<<<
triple_quote_para = '''
Hi I'm Sridhar!!,

How are you ?

'''
print(triple_quote_para)

# you can get the character from the string => stringVariable[index]
sample_string = 'I am Developer'
print(sample_string[0])  # 0 represents first character from left side of the string
print(sample_string[3])
print(sample_string[-1])  # -1 represents first character from right side of the string
print(sample_string[-7])

# you can get the substring from the main string => stringVariable[index1:index2]
# *** index2 is exclusive ***
print(sample_string[0:4])
print(sample_string[3:6])
print(sample_string[-5:-1])
print(sample_string[-5:-3])

# tricky indexes
# starts from 1st character and ends one character before from right
print(sample_string[1:-1])

print('-' * 10)

# python automatically takes index1 as 0, if you not mentioned index1
print(sample_string[:3])

# print all characters from index1 because it takes index2 is length of the string, if you not mentioned index2
print(sample_string[3:])

# to copy / clone one string to another you do like this
# it takes index1 is 0 and index2 is length of the string
anotherStr = sample_string[:]
print(anotherStr)

# =========================================
# >>>>> String Formatting <<<<<
# Formatted string syntax => f'{anyVariable}'
# f'{firstName} {lastName}' == firstName + ' ' + lastName
firstName = 'Python'
lastName = 'tutorial'
msg = f'Welcome to the {firstName} {lastName}!'
print(msg)
# Arguments by position
# The numbers inside the tuples represents the index of the elements in the format function call
print('{0} => {1} => {2}'.format(3, 'sri', True))
print('{1} => {0} => {2}'.format(3, 'sri', True))
my_tuple = (4, 'Rabbit', False)
print('{0}'.format(my_tuple))
# Arguments by name
print('I\'m {name} working as {work}'.format(work='Developer', name='Gadgeter'))
print('I\'m {name} working as {work}'.format(name='Gadgeter', work='Developer'))
# =========================================
# >>>>> String Methods <<<<<
dummyStr = 'python Tutorial pYthon'

print(len(dummyStr)) # Return the number of items in a container ( A container might be a String / List )
print(dummyStr.capitalize())  # Capitalize
print(dummyStr.upper())  # convert to upper case
print(dummyStr.lower())  # convert to lower case
print(dummyStr.swapcase())  # convert to swap case

# find the substring. Return index of the first match of the first letter of the substring if the substring matches. Otherwise, return -1
print(dummyStr.find('i'))
print(dummyStr.find('I'))
print(dummyStr.find('t'))
print(dummyStr.find('thoen'))

# replace
print(dummyStr.replace('Tutorial', 'Tutorials'))

# Returns true if it finds the substring in the main string. Otherwise, false
print('i' in dummyStr)
print('I' in dummyStr)
print('tori' in dummyStr)
print('Tori' in dummyStr)

# Count the occurrence of the substring
print(dummyStr.count('t'))
print(dummyStr.count('ho'))

# startswith & endswith
print(dummyStr.startswith('py'), dummyStr.startswith('Py'))
print(dummyStr.endswith('oN'), dummyStr.endswith('on'))

# split
print(dummyStr.split())

# Check for all Alphanumeric, all Alphabets, all Numeric
a = 'Python3'
b = 'Python 2'
c = 'Python'
d = '123'
print(a.isalnum(), b.isalnum(), c.isalnum(), d.isalnum())
print(a.isalpha(), b.isalpha(), c.isalpha(), d.isalpha())
print(a.isnumeric(), b.isnumeric(), c.isnumeric(), d.isnumeric())
