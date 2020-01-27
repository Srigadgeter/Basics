# >>>>> type conversion <<<<<
# string(number)/float/boolean to integer => int(<param>)
# string(number)/int/boolean to float => float(<param>)
# string/float/int to boolean => bool(<param>)
# To know about the type of variable => type(<anyVariable>)
birth_year = input('What is your Birth Year? ')
age = 2019 - int(birth_year) + 1
print('Your age is ', age)
print(type(birth_year))
print(type(age))
print(type(22), type(2.1), type(''), type(False))
print(
    int(232.3), int(True), int(False), int('123'),
    float(3), float(False), float(True), float('3'), float('3.4'),
    bool(2.1), bool(1), bool(0), bool(''), bool('a')
)
