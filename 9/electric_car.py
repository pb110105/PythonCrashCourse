#The __init__() method for the child class
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
#Instance as attribute
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__ (self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a state manting the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 60:
            range = 225
        else:
            range = 300
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make,model,year)
        #Defining Attributes and Methods for the Child Class
        self.battery = Battery()
    def describe_battery(self):
        """Print a statement describing the battery size."""
        #print(f"This car has a {self.battery_size}-kWh battery.")
        self.battery.describe_battery()
    #Overriding Methods from the Parent Class
    def fill_gas_tank(self):
        """Electric Cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
