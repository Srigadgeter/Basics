# >>>>> Filter & Map Functions <<<<<
items = [
    ('Note Book', 20),
    ('Pen', 30),
    ('Eraser', 5),
    ('Ruler', 15),
    ('Pencil', 8)
]

Filtered_items = list(filter(lambda item: item[1] > 10, items))
price_list = list(map(lambda item: item[1], items))
print(Filtered_items)
print(price_list)
# =========================================
# Lambda is a small anonymous function. It can take many arguments but can only have one expression.
sum_of_two_num = lambda num1, num2: num1 + num2
print(sum_of_two_num(2, 4))
