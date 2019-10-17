# print('SriGadgeter Gadgeter')
# print(1)
# print(2*8)
# print('*' * 8)
# print('*' + '33')
# print('=' * 20)
# print('a', 'b', '=' * 8, 3+4, True)
# # =========================================
# # >>>>> Boolean Values <<<<<
# # boolean values starts with Capital letter => False / True
# variable_a = False
# variable_b = True
# print(variable_a, variable_b)
# # =========================================
# # >>>>> input prompt <<<<<
# name = input('What is your name? ')
# color = input('What is your favourite color? ')
# print(name + ' likes ' + color)
# # =========================================
# # >>>>> type conversion <<<<<
# # string(number)/float/boolean to interger => int(<param>)
# # string(number)/int/boolean to float => float(<param>)
# # string/float/int to boolean => bool(<param>)
# # To know about the type of varibale => type(<anyVariable>)
# birth_year = input('What is your Birth Year? ')
# age = 2019 - int(birth_year)
# print(age)
# print(type(birth_year))
# print(type(age))
# print(type(22), type(2.1), type(''), type(False))
# print(int(232.3), int(True), int(False), int('123'), float(3), float(False), float(True), float('3'), float('3.4'), bool(2.1), bool(1), bool(0), bool(''), bool('a'))
# # =========================================
# # >>>>> Strings <<<<<
# triple_quote_para = '''
# Hi I'm Sridhar!!,
#
# How are you ?
#
# '''
# print(triple_quote_para)
#
# # you can get the character from the string => stringVariable[index]
# sample_string = 'I am Developer'
# print(sample_string[0])  # 0 represents first character from left side of the string
# print(sample_string[3])
# print(sample_string[-1])  # -1 represents first character from right side of the string
# print(sample_string[-7])
#
# # you can get the substring from the main string => stringVariable[index1:index2]
# # *** index2 is exclusive ***
# print(sample_string[0:4])
# print(sample_string[3:6])
# print(sample_string[-5:-1])
# print(sample_string[-5:-3])
#
# # tricky indexes
# # starts from 1st character and ends one character before from right
# print(sample_string[1:-1])
#
# print('-' * 10)
#
# # python automatically takes index1 as 0, if you not mentioned index1
# print(sample_string[:3])
#
# # print all characters from index1 because it takes index2 is length of the string, if you not mentioned index2
# print(sample_string[3:])
#
# # to copy / clone one string to another you do like this
# # it takes index1 is 0 and index2 is length of the string
# anotherStr = sample_string[:]
# print(anotherStr)
#
# # =========================================
# # >>>>> String Formatting <<<<<
# # Formatted string syntax => f'{anyVariable}'
# # f'{firstName} {lastName}' == firstName + ' ' + lastName
# firstName = 'Python'
# lastName = 'tutorial'
# msg = f'Welcome to the {firstName} {lastName}!'
# print(msg)
# # Arguments by position
# # The numbers inside the tuples represents the index of the elements in the format function call
# print('{0} => {1} => {2}'.format(3, 'sri', True))
# print('{1} => {0} => {2}'.format(3, 'sri', True))
# my_tuple = (4, 'Rabbit', False)
# print('{0}'.format(my_tuple))
# # Arguments by name
# print('I\'m {name} working as {work}'.format(work='Developer', name='Gadgeter'))
# print('I\'m {name} working as {work}'.format(name='Gadgeter', work='Developer'))
# # =========================================
# # >>>>> String Methods <<<<<
# dummyStr = 'python Tutorial pYthon'
#
# print(len(dummyStr)) # Return the number of items in a container ( A container might be a String / List )
# print(dummyStr.capitalize())  # Capitalize
# print(dummyStr.upper())  # convert to upper case
# print(dummyStr.lower())  # convert to lower case
# print(dummyStr.swapcase())  # convert to swap case
#
# # find the substring. Return index of the first match of the first letter of the substring if the substring matches. Otherwise, return -1
# print(dummyStr.find('i'))
# print(dummyStr.find('I'))
# print(dummyStr.find('t'))
# print(dummyStr.find('thoen'))
#
# # replace
# print(dummyStr.replace('Tutorial', 'Tutorials'))
#
# # Returns true if it finds the substring in the main string. Otherwise, false
# print('i' in dummyStr)
# print('I' in dummyStr)
# print('tori' in dummyStr)
# print('Tori' in dummyStr)
#
# # Count the occurrence of the substring
# print(dummyStr.count('t'))
# print(dummyStr.count('ho'))
#
# # startswith & endswith
# print(dummyStr.startswith('py'), dummyStr.startswith('Py'))
# print(dummyStr.endswith('oN'), dummyStr.endswith('on'))
#
# # split
# print(dummyStr.split())
#
# # Check for all Alphanumeric, all Alphabets, all Numeric
# a = 'Python3'
# b = 'Python 2'
# c = 'Python'
# d = '123'
# print(a.isalnum(), b.isalnum(), c.isalnum(), d.isalnum())
# print(a.isalpha(), b.isalpha(), c.isalpha(), d.isalpha())
# print(a.isnumeric(), b.isnumeric(), c.isnumeric(), d.isnumeric())
# # =========================================
# # >>>>> Arithmetic operations <<<<<
# # / => division
# # // => quotient
# # % => remainder
# # ** => exponential (power of) operator
# print(10/3, 10//3, 10%3, 10**3)
# # =========================================
# # >>>>> Operator Precedence <<<<<
# # Order of operations => parenthesis, exponentiation, multiplication/division , addition/subtraction
# print(10 + 5 * 3 ** 2)
# # =========================================
# # >>>>> Math Functions <<<<<
# print(abs(-322.22), round(2.33))
# import math
# print(math.ceil(2.3), math.floor(2.3), math.sqrt(256))
# # =========================================
# # >>>>> if/elif/else <<<<<
# marks = 80
#
# if marks & marks <=100:
#     if marks > 35:
#         print('You passed')
#     elif marks < 35:
#         print('You failed')
#     else:
#         print('You just passed')
# else:
#     print('Marks awarded only less than or equal to 100')
# # =========================================
# # >>>>> Logical Operators <<<<<
# # and, or, not
# has_passed_marks = True
# has_bad_conduct = False
#
# if has_passed_marks and not has_bad_conduct:
#     print('Eligible for Good colleges')
# elif has_passed_marks or not has_bad_conduct:
#     print('Eligible for Moderate colleges')
# else:
#     print('Eligible for worst colleges')
# # =========================================
# # >>>>> While Loops <<<<<
# i = 1
# while i <= 3:
#     print('@' * i, i)
#     i = i + 1
# print('While ends & this statement is out of while loop')
# # =========================================
# # Game 1
# secret_number = 3
# guess_count = 1
# guess_limit = 3
# print('You have three chances to guess the secret number occur between 0 and 10')
# # else block for the while loop will execute after the while loop iterations finished
# # else block for the while loop won't execute if the while loop breaks in the middle of iterations
# while guess_count <= guess_limit:
#     guess = int(input('Guess ' + str(guess_count) + ': '))
#     if guess == secret_number:
#         print('You Found :)')
#         break
#     else:
#         guess_count += 1
# else:
#     print('You guessed wrong for the given chances :(')
# # =========================================
# # Game 2
# isQuit = False
# isBikeStarted = False
# print('Game started')
# while not isQuit:
#     entered_command = input('> ').lower()
#     if entered_command == 'quit':
#         print('You quit the game')
#         isQuit = True
#     elif entered_command == 'help':
#         print('''
# Commands List to operate the bike:
#     help - To see the commands list
#     start - To start the bike
#     stop - To stop the bike
#     quit - To exit the game
#         ''')
#     elif entered_command == 'start':
#         if isBikeStarted == True:
#             print('Yeah, Bike is already started')
#         else:
#             isBikeStarted = True
#             print('Bike started... Ride speed to get thrill')
#     elif entered_command == 'stop':
#         if not isBikeStarted == True:
#             print('Yeah, Bike is already stopped')
#         else:
#             isBikeStarted = False
#             print('Bike stopped')
#     else:
#         print("I don't understand your command")
# # =========================================
# # >>>>> For Loops <<<<<
# for item in 'Gamer':
#     print(item)
# print('-------')
# for item in ['i', 'am', 'python', 'programmer']:
#     print(item)
# print('-------')
# # range(start_number, end_number, increment_number) <<== end_number is exclusive
# for item in range(5):
#     print(item)
# print('-------')
# for item in range(5, 10):
#     print(item)
# print('-------')
# for item in range(2, 10, 3):
#     print(item)
# print('-------')
# for x in range(3):
#     for y in range(2):
#         print(f'({x}, {y})')
# print('-------')
# for x in [5, 2, 5, 2, 2]:
#     liner = ''
#     for y in range(x):
#         liner += 'x'
#     print(liner)
# print('-------')
# # =========================================
# # >>>>> Lists <<<<<
# names = ['Sri', 'Gadgeter', 'Sridhar', 'Srigadgeter']
# print(names)
# print(names[1])
# print(names[1:3])
# print(names[-2])
# print(names[-2:])
# print(names[:3])
# print(names[:])
# names[3] = 'SriGadgeter'
# print(names)
# print('-------')
# print(names[2][1])
# print(names[1][1:])
# print(names[0][-2:])
# print(names[2][:2])
# # =========================================
# # >>>>> 2D Lists <<<<<
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0])
# print(matrix[1:])
# print(matrix[-1:])
# print(matrix[:])
# print('-------')
# print(matrix[0][0])
# print(matrix[2][2])
# print(matrix[1][2])
# print('-------')
# print(matrix[0][1:])
# print('-------')
# names = [
#     ['abc', 'def', 'ghi', 'jkl'],
#     ['mno', 'pqr', 'stu', 'vwx'],
#     ['yz~', '!@#', '$%^', '&*-']
# ]
# print(names)
# print(names[2])
# print(names[1][2:])
# print('-------')
# print(names[2][1])
# print(names[1][:2])
# print('-------')
# print(names[1][0][-1])
# print(names[1][3][1:])
# print(names[1][1][-3:-1])
# # =========================================
# # >>>>> List Methods <<<<<
# numbers = [3, 4, 9, 0, 2, 6, 4]
# numbers.append(8)  # Add a new element @ last
# numbers.insert(0, 8)  # Add a new element @ the given position
# numbers.insert(4, 8)
# numbers.remove(9)  # Remove the element based on value
# numbers.clear()  # Remove all the elements in the list
# numbers.pop()  # Remove the last element
# numbers.pop(2)  # Remove the element based on index
# numbers.sort()  # Sort A -> Z
# numbers.sort(reverse=True)  # Sort Z -> A (Reverse Sort)
# numbers.reverse()  # Reverse the list
# print(numbers)
# print('-------')
# numbers2 = numbers.copy()
# numbers3 = numbers[:]
# numbers.append(32)
# print(numbers, numbers2, numbers3)
# print('-------')
# print(numbers.index(4)) # Prints the first occurrence of the given element
# print(numbers.index(5)) # And it will throw an ValueError if there is no such element in the list
# print(4 in numbers, 5 in numbers)
# print(numbers.count(4)) # Prints the number of occurrences of the given element
# print(numbers.count(9))
# print(numbers.count(5))
# # =========================================
# # >>>>> Tuples <<<<<
# # Tuple is an immutable ( It allows duplicate values )
# # Create tuple in literal way (direct assignment)
# tuple_numbers = (2, 5, 3)
# print(tuple_numbers[1])
#
# # Create tuple using constructor
# tuple_num = tuple([1, 2, 5])  # From list
# tuple_num2 = tuple((1, 2, 5))  # From tuple
# tuple_num3 = tuple({1, 2, 5})  # From set
# print(tuple_num, tuple_num2, tuple_num3)
#
# # This line leads to an error => TypeError: 'tuple' object does not support item assignment
# Can't change any value in the tuple because it is immutable
# tuple_numbers[0] = 23
#
# # Tuple have one value should have trailing comma
# tuple_2 = ('a',)
# print(tuple_2)
#
# # Length of Tuple
# print(len(tuple_numbers), len(tuple_2))
#
# # Can't delete the element in the tuple
# # Below line will result in error => TypeError: 'tuple' object doesn't support item deletion
# del tuple_2[0]
#
# # Delete the tuple
# del tuple_2
''' 
The below print leads to error => NameError: name 'tuple_2' is not defined.
Because we deleted the tuple_2 in the above line
'''
# print(tuple_2)
# # =========================================
# # >>>>> Unpacking <<<<<
# tuple_numbers = (4, 1, 0)
# x, y, z = tuple_numbers
# s, t = [3, 4]
# print(x,y,z,s,t)
# # =========================================
# # >>>>> Dictionaries <<<<<
# # Dictionary is a collection which unordered, indexed & changeable with no duplicates.
# person = {
#     'name': 'Gamer',
#     'age': 22,
#     'is_married': False
# }
#
# # Create dictionary using constructor
# person2 = dict(firs_name='Sri', last_name='Gadgeter', age=22)
# person3 = dict([('name', 'Gadgeter'), ('age', 23), ('is_married', True)])  # From list of tuples
# print(person2, person3)
#
# # Access value for the key
# print(person['age'])
# print(person['dob']) # It will throw an KeyError if the key doesn't exist in the given dictionary
# print(person.get('name'))
# print(person.get('father_name')) # It will print 'None' if the key doesn't exist in the given dictionary
# person['name'] = 'Gadgeter' # update existing key
# person['dob'] = 'dd-mm-yyyy' # add a new key
#
# # Provide default value
# print(person.get('father_name', 'GamerFather')) # We can show a default value for non-existing key
# print(person)
#
# # Get all keys from the dictionary
# print(person.keys())
#
# # Get all values from the dictionary
# print(person.values())
#
# # Get all key-value pairs from the dictionary
# print(person.items())
#
# # Make a copy
# person_copy = person.copy()
# print(person_copy)
#
# # Delete a key-value pair using key
# del(person_copy['age'])
# print(person_copy)
#
# # Delete the dictionary
# del person_copy
# print(person_copy)  # This results in error => NameError: name 'person_copy' is not defined
#
# # Remove a key-value pair using key
# person_copy.pop('name')
# print(person_copy)
#
# # Clear the dictionary
# person_copy.clear()
# print(person_copy)
#
# # Length of the dictionary
# print(len(person_copy))
#
# # List of dictionary
# people = [person, person3]
# print(people)
# print(people[0]['name'], people[1]['name'])
# # =========================================
# # Dictionary Game
# numbers_in_words = {
#     0: 'Zero',
#     1: 'One',
#     2: 'Two',
#     3: 'Three',
#     4: 'Four',
#     5: 'Five',
#     6: 'Six',
#     7: 'Seven',
#     8: 'Eight',
#     9: 'Nine',
# }
# phone_number = input('Phone Number please: ')
# phone_number_in_words = ''
# for number in phone_number:
#     phone_number_in_words += f'{numbers_in_words[int(number)]} '
# print(phone_number_in_words)
# # =========================================
# # Emoji Converter Game
# emojies = {
#     ':)': '😄',
#     ':(': '😢',
# }
#
# while True:
#     message = input('> ')
#     if message == 'quit':
#         print('You quit the Emoji Converter')
#         break
#     else:
#         messages = message.split(' ')
#         converted_msg = ''
#         for msg in messages:
#             converted_msg += f'{emojies.get(msg, msg)} '
#         print(converted_msg)
# # =========================================
# # >>>>> Functions <<<<<
# def greeting(age, first_name, last_name):
#     return f'Welcome, {first_name} {last_name} is {age}'
#
#
# print(greeting(22, 'Sri', 'Gadgeter'))
# print(greeting(22, last_name='Gadgeter', first_name='Sri')) # keyword arguments
# # =========================================
# # >>>>> Exceptions <<<<<
# try:
#     age = int(input('Age: '))
#     income = 10000
#     risk = income / age
#     print(f'Your risk according to your age is {risk}')
# except ValueError:
#     print('Invalid value')
# except ZeroDivisionError:
#     print('The age should be greater than 0')
# # =========================================
# # >>>>> Classes <<<<<
# class Point:
#     # __init__ function is constructor of the class
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print('Move the Point')
#
#     def draw(self):
#         print('Draw the Point')


# point1 = Point()
# point1.x = 1
# point1.y = 3
# print(point1.x, point1.y)
# point1.move()
# point1.draw()

# Point2 = Point
# print(Point2)
# point3 = Point2()
# print(point3)

# print('-------')
# point4 = Point(3, 5)
# print(point4.x, point4.y)

# point5 = Point(3, 5)
# point5.x = 2
# print(point5.x, point5.y)
# # =========================================
# # >>>>> Classes - Inheritance <<<<<
# class Mammal:
#     def walk(self):
#         print('walk')
#
#
# # Dog extends Mammal class
# class Dog(Mammal):
#     pass # pass keyword used when we leave a class empty because class should be empty
#
#
# # Cat extends Mammal class
# class Cat(Mammal):
#     def meow(self):
#         print('meow.. meow..')
#
#
# dog = Dog()
# dog.walk()
#
# cat = Cat()
# cat.walk()
# cat.meow()
# # =========================================
# # >>>>> Modules <<<<<
# # Below import statement imports the entire converters module
# import converters
#
# # we should call the functions inside module like module_name.function_name
# print(converters.celcius_to_farenheit(0))
# print(converters.celcius_to_farenheit(3))
#
# print(converters.farenheit_to_celcius(35.6))
# print(converters.farenheit_to_celcius(0))
# print('-------')
# from converters import celcius_to_farenheit
#
# print(celcius_to_farenheit(4))
# # =========================================
# # >>>>> Packages <<<<<
# import ecommerce.shipping
#
# ecommerce.shipping.shipping_calculation()
# ecommerce.shipping.tax_calculation()
# print('-------')
# from ecommerce import shipping
#
# shipping.shipping_calculation()
# shipping.tax_calculation()
# print('-------')
# from ecommerce.shipping import shipping_calculation, tax_calculation
#
# shipping_calculation()
# tax_calculation()
# # =========================================
# # >>>>> Generating Random Values <<<<<
# import random
#
# aa = random.random() # Random float:  0.0 <= n < 1.0
# bb = random.randint(5, 10) # Random integer: a <= n <= b (Here a = 5, b = 10)
# cc = None
# roles = ['gadgeter', 'gamer', 'developer', 'designer']
# try:
#     cc = random.choice(roles) # Randomly pick one from the list
# except IndexError:
#     print('List should not be empty')
#
# print(aa, bb, cc)
# # =========================================
# # >>>>> Random - Dice Game <<<<<
# from Dice import Dice
#
# dice1 = Dice()
# dice2 = Dice()
#
# print(f'({dice1.roll()}, {dice2.roll()})')
# # =========================================
# # >>>>> Files & Directories <<<<<
# from pathlib import Path

###
# Two types of paths
# 1 Absolute Path - path of any file/directory in our hard disk
# 2 Relative Path - path inside project's root folder
###

# path1 = Path('email')
#
# if path1.exists():
#     path1.rmdir()
# else:
#     path1.mkdir()
#
# print('-------')
#
# path2 = Path() # Without any arguments which represents the Current Project's Root Directory
# files = path2.glob('*.py') # searching files endswith '.py' extension inside the root directory
#
# for file in files:
#     print(file)
#
# files2 = path2.glob('*') # searching all files & folders inside the root directory
#
# for file in files2:
#     print(file)
# # =========================================
# # >>>>> Ternary Operation <<<<<
# # syntax: <if_block> if <condition> else <else_block>
# age = 20
# isEligible = 'Eligible' if age >= 18 else 'Not eligible'
# print(isEligible)
# # =========================================
# # >>>>> Chaining Comparison Operators <<<<<
# age = 17
# print(18 <= age < 65)
# # =========================================
# # *args
# # we can pass multiple parameter if we use *argument_name in function definition
# def multi_arguments(*numbers):
#     print(numbers)
#
#
# multi_arguments(2, 3, 5, 6, 7)
# # =========================================
# # **args
# # we can pass multiple keyword arguments if we use **argument_name in function definition
# def multi_keyword_arguments(**user):
#     print(user)
#     print(user['id'], user['name'], user['age'])
#
#
# multi_keyword_arguments(id=1, age=20, name='gadgeter')
# # =========================================
# # >>>>> Sets <<<<<
# # Set is a unordered & non-indexed collection of unique elements
#
# # Create set using constructor
# uniques1 = set([1, 12, 33, 3, 23, 33, 44])  # From list
# uniques2 = set((1, 12, 33, 3, 23, 33, 44))  # From tuple
# print(uniques1, uniques2)
#
# set1 = {3, 5, 1}
# # Add an item to the set
# set1.add(4)
# set1.add(3)  # The number 3 is already present. So it wont add
#
# # Remove an item from the set
# set1.remove(5)  # Remove an item by value
# print(set1)
#
# # Clear the set
# set1.clear()
# print(set1)
#
# # Delete the set
# del set1
# print(set1)  # Will result in error => NameError: name 'set1' is not defined
#
# # union of two sets
# union = uniques | set1
# print(union)
#
# # intersection of two sets
# intersection = uniques & set1
# print(intersection)
#
# # element presents in either first or second & not both of two sets
# not_both = uniques ^ set1
# print(not_both)
#
# # difference of two sets
# difference1 = uniques - set1
# difference2 = set1 - uniques
# print(difference1, difference2)
# # =========================================
# # >>>>> Filter & Map Functions <<<<<
# items = [
#     ('Note Book', 20),
#     ('Pen', 30),
#     ('Eraser', 5),
#     ('Ruler', 15),
#     ('Pencil', 8)
# ]
#
# Filtered_items = list(filter(lambda item: item[1] > 10, items))
# price_list = list(map(lambda item: item[1], items))
# print(Filtered_items)
# print(price_list)
# # =========================================
# # Lambda is a small anonymous function. It can take many arguments but can only have one expression.
# sum_of_two_num = lambda num1, num2: num1 + num2
# print(sum_of_two_num(2, 4))
# # =========================================
# # Membership operator (in, not in)
# # Identity operator (is, is not)
# # =========================================
# # >>>>> Filter & Map Functions <<<<<

