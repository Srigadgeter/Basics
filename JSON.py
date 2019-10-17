# >>>>> JSON - JavaScript Object Notation <<<<<

import json

# Parsing json to dictionary
# json => dictionary
my_json_data = '{"name": "Gadgeter", "role": "Developer", "age": 22}'  # Properties should enclosed with double quotes
dict_data = json.loads(my_json_data)
print(dict_data)


# dictionary => json
my_dict_data = {
    'name': 'BMW',
    'price': 1000000,
    'can_race': True
}
json_data = json.dumps(my_dict_data)
print(json_data)
