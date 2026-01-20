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