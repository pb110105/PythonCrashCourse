#5-1. Conditional Tests
car = 'subaru'
anime = ['one piece', 'naruto', 'bleach', 'attack on titan', 'demon slayer']
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')
print("\n Is car == 'audi'? I preddict False")
print(car == 'audi')
print('one piece' in anime)
print('dragon ball' in anime)
print('dragon ball' not in anime)
print('bleach' not in anime)
print('naruto' in anime)
print('naruto' not in anime)
print('attack on titan' in anime)
print('attack on titan' not in anime)
print('demon slayer' in anime)
print('demon slayer' not in anime)
#5-2. More Conditional Tests
animal = 'naruto'
numbers = [10, 20, 30, 40, 50]
print(animal == 'naruto')
print(animal != 'naruto')
print(animal.lower() == 'naruto')
number = 24
print(number == 24)
print(number != 24)
print(number > 20)
print(number < 30)
print(number >= 24)
print(number <= 24)
print(number >= 25 and number <= 30)
print(number >= 20 or number <= 23)
print('20' in str(numbers))
print('25' not in str(numbers))
#5-3. Alien Colors #1
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points")

if alien_color == 'green':
    print("Yes")
else:
    None
#5-4. Alien Colors #2
if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien")
if alien_color != 'green':
    print("The player just earned 10 points")
if alien_color == 'green':
    print("The player plaplapla")
else:
    print("The player oooo")
#5-5. Alien Colors #3
if alien_color == 'green':
    print("Green")
elif alien_color == 'red':
    print("red")
else:
    print("yellow")
#5-6 Stage of life
age = 10
if age < 2:
    print("Baby")
elif age >= 2 and age < 4:
    print("Toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    print("elder")
#5-7. Favorite Fruit
favorite_fruits = ['apple', 'banana', 'mango']
if 'banana' in favorite_fruits:
    print("You really like banana!")
#5-8. Hello Admin
username = ['admin', 'bao', 'anh', 'hung', 'trang']
for name in username:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")
#5-9. No Users
username = []
if username:
    for name in username:
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")
#5-10. Checking Usernames
current_users = ['bao', 'anh', 'hung', 'trang', 'linh']
new_users = ['nam', 'hoa', 'bao', 'linh', 'tuan']
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"{new_user} has been used, please enter a new username.")
    else:
        print(f"{new_user} is available.")
#5-11. Ordinal Numbers
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
#5-12. Styling if statements
if age > 2:
    print("Child")
#5-13. Your Ideas
animals = ['dog', 'cat', 'rabbit', 'zebra', 'giraffe', 'elephant']
for animal in animals:
    if 'lion' in animal:
        print(f"{animal} is the king of the jungle.")
    else:
        print(f"{animal} is a wonderful animal.")