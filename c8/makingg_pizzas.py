import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(112, 'mushhroom', 'green peppers', 'extra cheese')
#Importing Specific Funtions
#Using as to Give a Funtion an Alias
from pizza import make_pizza as mp
mp(16, 'meomeo')
mp(20, 'to')
#Using as to Give a Module an Alias
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#Importing All Funtions in a Module
from pizza import *
make_pizza(11, 'pep')
make_pizza(12, 'mushrooms','grren che', 'extra')
#Styling funtions