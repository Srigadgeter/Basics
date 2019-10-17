print('SriGadgeter Gadgeter')
print(1)
print(2*8)
print('*' * 8)
print('*' + '33')
print('=' * 20)
print('a', 'b', '=' * 8, 3+4, True)
# =========================================
# >>>>> Boolean Values <<<<<
# boolean values starts with Capital letter => False / True
variable_a = False
variable_b = True
print(variable_a, variable_b)
# =========================================
# >>>>> input prompt <<<<<
name = input('What is your name? ')
color = input('What is your favourite color? ')
print(name + ' likes ' + color)
# =========================================
# >>>>> Arithmetic operations <<<<<
# / => division
# // => quotient
# % => remainder
# ** => exponential (power of) operator
print(10/3, 10//3, 10%3, 10**3)
# =========================================
# >>>>> Operator Precedence <<<<<
# Order of operations => parenthesis, exponentiation, multiplication/division , addition/subtraction
print(10 + 5 * 3 ** 2)
# =========================================
# >>>>> Math Functions <<<<<
print(abs(-322.22), round(2.33))
import math
print(math.ceil(2.3), math.floor(2.3), math.sqrt(256))
# =========================================
# **args
# we can pass multiple keyword arguments if we use **argument_name in function definition


def multi_keyword_arguments(**user):
    print(user)
    print(user['id'], user['name'], user['age'])


multi_keyword_arguments(id=1, age=20, name='gadgeter')
# =========================================
# Membership operator (in, not in)
# Identity operator (is, is not)
# =========================================
