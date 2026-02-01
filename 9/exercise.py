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