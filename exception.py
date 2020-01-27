# >>>>> Exceptions <<<<<
try:
    age = int(input('Age: '))
    if age > 0:
        income = 10000
        risk = income / age
        print(f'Your risk according to your age is {risk}')
    else:
        print('You should not provide the negative value for age')
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('The age should be greater than 0')
