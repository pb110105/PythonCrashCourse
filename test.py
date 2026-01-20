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