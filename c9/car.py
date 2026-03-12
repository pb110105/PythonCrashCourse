#Working with classes and instances
#The car class
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
my_new_car = Car('audi', 'a4', '2024')
print(my_new_car.get_descriptive_name())
#Setting a Default Value for an Attribute
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing a car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
my_new_car = Car('audi', 'a4', '2024')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
#Modifying Attribute Values
#Modifying an Attribute's Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#Modifying an Attribute's Value Through a Method
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing a car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You don't roll back an adometer!")
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
my_new_car = Car('audi', 'a4', '2024')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
#Importing Classes
#Imoporting a Single Class
"""A Class that can be used to represent a car."""
#Storing Multiple classes in a Module
class Car:
    """A simple attempt to represent a car. """
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing a car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You don't roll back an adometer!")
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
