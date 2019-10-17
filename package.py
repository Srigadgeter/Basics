# >>>>> Packages <<<<<
import ecommerce.shipping

ecommerce.shipping.shipping_calculation()
ecommerce.shipping.tax_calculation()

from ecommerce import shipping

shipping.shipping_calculation()
shipping.tax_calculation()

from ecommerce.shipping import shipping_calculation, tax_calculation

shipping_calculation()
tax_calculation()
# =========================================
# >>>>> Generating Random Values (By importing the package called random) <<<<<
import random

aa = random.random() # Random float:  0.0 <= n < 1.0
bb = random.randint(5, 10) # Random integer: a <= n <= b (Here a = 5, b = 10)
cc = None
roles = ['gadgeter', 'gamer', 'developer', 'designer']
try:
    cc = random.choice(roles) # Randomly pick one from the list
except IndexError:
    print('List should not be empty')

print(aa, bb, cc)
# =========================================
# >>>>> Random - Dice Game <<<<<
from Dice import Dice

dice1 = Dice()
dice2 = Dice()

print(f'({dice1.roll()}, {dice2.roll()})')
