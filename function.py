# >>>>> Functions <<<<<
def greeting(age, first_name, last_name):
    return f'Welcome, {first_name} {last_name} is {age}'


print(greeting(22, 'Sri', 'Gadgeter'))
print(greeting(22, last_name='Gadgeter', first_name='Sri'))  # keyword arguments
