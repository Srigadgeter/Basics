# >>>>> Exceptions <<<<<
try:
    age = int(input('Age: '))
    income = 10000
    risk = income / age
    print(f'Your risk according to your age is {risk}')
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('The age should be greater than 0')
