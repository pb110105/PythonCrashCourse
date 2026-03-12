#9-1. Restaurant
class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"You choose {self.restaurant_name} and {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The {self.restaurant_name} is opening")
my_restaurant = restaurant("Dookie", "Buffet")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
#9-2. Three Restaurant
restaurant_1 = restaurant("Chiki", "Pochin")
restaurant_1.describe_restaurant()
restaurant_2 = restaurant("Super", "meomeo")
restaurant_2.describe_restaurant()
restaurant_3 = restaurant("Lucas", "Hapis")
restaurant_3.describe_restaurant()
#9-3. Users
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
User1 = User("Bao", "Pham")
User1.describe_user()
User1.greet_user()
User2 = User("Anh", "Nguyen")
User2.describe_user()
User2.greet_user()
User3 = User("Anh", "Pham")
User3.describe_user()
User3.greet_user()
#9-4. Number Served
class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"You choose {self.restaurant_name} and {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The {self.restaurant_name} is opening")
    def set_number_served(self):
        self.number_served = 25
        print(f"Number of customers served: {self.number_served}")
    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers
        print(f"Number of customers served: {self.number_served}")
my_restaurant = restaurant("Dookie", "Buffet")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served()
my_restaurant.increment_number_served(30)
#9-5. Login Attempts
class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
    def increment_login_attempts(self):
        self.login_attempts = 0
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts reset to: {self.login_attempts}")

User1 = User("Bao", "Pham", 0)
User1.describe_user()
User1.greet_user()
User1.increment_login_attempts()
User1.reset_login_attempts()
User2 = User("Anh", "Nguyen", 0)
User2.describe_user()
User2.greet_user()
User3 = User("Anh", "Pham", 0)
User3.describe_user()
User3.greet_user()
#9-6. Ice Cream Stand
class IceCreamStand(restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vani', 'choco', 'matcha']
    def display_flavors(self):
        print(f"Available flavors: {self.flavors}")
ice_cream =  IceCreamStand("Each", "Ice Cream")
ice_cream.describe_restaurant()
ice_cream.display_flavors()
#9-7 Admin
class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = ['can add post', 'can delete', 'can ban user']
    def show_privileges(self):
        print(f"Admin privileges: {self.privileges}")
admin_user = Admin("Admin", "User", 0)
admin_user.describe_user()
admin_user.show_privileges()
#9-8. Privileges
class Privileges:
    def __init__(self, privileges = []):
        self.privileges = privileges
    def show_privileges(self):
        print(f"Admin privileges: {self.privileges}")
class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges(['can add post', 'can delete', 'can ban user'])
admin_user = Admin("Admin", "User", 10)
admin_user.describe_user()
admin_user.privileges.show_privileges()
#9-9. Battery Upgrade
print("9-9. Battery Upgrade")
import electric_car as ec
my_tesla = ec.ElectricCar('tesla', 'model s', 2024)
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
#9-10. Imported Restaurant
my_restaurant = restaurant("Dookie", "Buffet")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
#9-11. Imported Admin
admin_user = Admin("admin", "user", 0)
admin_user.describe_user()
admin_user.privileges.show_privileges()
#9-12. Multiple Modules
from dog import Dog
from car import Car
action_dog = Dog("barry", 3)
action_dog.sit()
action_dog.roll()
#9-13. Dice
from random import randint
class Die: 
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(f"Random number: {randint(1, self.sides)}")
six_sided_die = Die()
six_sided_die.roll_die()
ten_sided_die = Die(10)
ten_sided_die.roll_die()
twenty_sided_die = Die(20)
twenty_sided_die.roll_die()
#9-14. Lottery
lottery = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
from random import choice
print(f"Lottery result: {choice(lottery)}{choice(lottery)}{choice(lottery)}{choice(lottery)}")
#9-15. Lottery Analysis
my_ticket = [1,2,3,4,5]
win_lottery = [choice(lottery) for _ in range(12)]
matches = 0
for number in my_ticket:
    if number in win_lottery:
        matches += 1
print(f"Number of matches: {matches}")
#9-16. Python Module of the Week
#Nothing to do for this exercise, but you can visit the Python Module of the Week website at https://pymotw.com/ to explore the standard library and find modules that interest you.