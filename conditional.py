# >>>>> if/elif/else <<<<<
marks = 80

if marks & marks <=100:
    if marks > 35:
        print('You passed')
    elif marks < 35:
        print('You failed')
    else:
        print('You just passed')
else:
    print('Marks awarded only less than or equal to 100')
# =========================================
# >>>>> Logical Operators <<<<<
# and, or, not
has_passed_marks = True
has_bad_conduct = False

if has_passed_marks and not has_bad_conduct:
    print('Eligible for Good colleges')
elif has_passed_marks or not has_bad_conduct:
    print('Eligible for Moderate colleges')
else:
    print('Eligible for worst colleges')
