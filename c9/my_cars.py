#Importing Multiple Classes from a Module
from electric_car import Car, ElectricCar
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
#Importing an Entire Module
print("-----")
import electric_car
my_mustang = electric_car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = electric_car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

print("-----")
from car import Car
from electric_car import ElectricCar
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
#Using Aliases
print("-----")
from electric_car import ElectricCar as EC
my_leaf = EC('nissan', 'leaf', 2024)
import electric_car as ec
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
