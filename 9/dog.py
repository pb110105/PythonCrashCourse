#Creating and Using a Class
#Create the Dog Class
class Dog:
    """A simple pattern to model a dog"""
    def __init__(self, name, age):
        """Initilize name and age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """Stimulate a do g sitting in response to a command"""
        print(f"{self.name} is now sitting")
    def roll(self):
        """Stimulate rolling over in response to a command"""
        print(f"{self.name} rolled over")
#The __init__() Method
#Making an Instances from a Class
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll()
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old")
#Accessing Attribbutes
#Calling Methods
#Creating Multiple Instances
print("-----")
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old")
my_dog.sit()
print(f"\n Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} year old")
your_dog.sit()