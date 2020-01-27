# >>>>> Chaining Comparison Operators <<<<<


def am_i_major(age):
    return 18 <= age < 65


print(am_i_major(17))
print(am_i_major(23))
# =========================================
# *args
# we can pass multiple parameter if we use *argument_name in function definition


def multi_arguments(*numbers):
    print(numbers)


multi_arguments(2, 3, 5, 6, 7)
