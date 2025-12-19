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