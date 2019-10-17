# >>>>> Chaining Comparison Operators <<<<<
age = 17
print(18 <= age < 65)
# =========================================
# *args
# we can pass multiple parameter if we use *argument_name in function definition


def multi_arguments(*numbers):
    print(numbers)


multi_arguments(2, 3, 5, 6, 7)
