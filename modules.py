# >>>>> Modules <<<<<
# Below import statement imports the entire converters module
import converters

# we should call the functions inside module like module_name.function_name
print(converters.celcius_to_farenheit(0))
print(converters.celcius_to_farenheit(3))

print(converters.farenheit_to_celcius(35.6))
print(converters.farenheit_to_celcius(0))

from converters import celcius_to_farenheit

print(celcius_to_farenheit(4))
