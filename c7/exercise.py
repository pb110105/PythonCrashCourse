#7-1. Rental Car
car = input("What kind of rental car would you like? ")
print(f"\nLet me see if I can find you a {car}.")
#7-2. Restaurant Seating
people = input("How many people are in your dinner group? ")
people = int(people)
if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
#7-3. Multiples of Ten
number = input("Enter a number and I'll tell you if it's a multiple of ten: ")
number = int(number)
if number % 10 == 0:
    print(f"\n The number {number} is a multiple of ten")
#7-4. Pizza Toppings
while True:
    topping = input("\nPlease enter topping for pizza: ")
    if topping == 'quit':
        break
    else:
        print(f"\tI will add {topping} topping to your pizza")
#7-5. Movie Tickets
age = input("Enter you age: ")
age = int(age)
while True:
    if age < 3:
        print("The ticket is free")
    elif age >= 3 and age <= 12:
        print("The ticket is $10")
    elif age > 12:
        print("The ticket is $15")
    break
#7-6. Three Exits
age = input("Enter you age: ")
age = int(age)
while True:
    if age < 3:
        print("The ticket is free")
        break
    elif age >= 3 and age <= 12:
        print("The ticket is $10")
        break
    elif age > 12:
        print("The ticket is $15")
        break
#7-7. Infinity
x = 1
while x == 1:
    print(x)
#7-8. Deli
sandwich_orders = ['tuna', 'lika', 'nika', 'rika']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
#7-9. No Pastrami
sandwich_orders = ['tuna','pastrami', 'lika','pastrami', 'nika', 'rika', 'pastrami']
finished_sandwiches = []
while sandwich_orders:
    print("\n The deli has run out of pastrami")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
#7-10. Dream Vacation
dream_vacation = {}
while True:
    name = input("\nEnter your name")
    vacation = input("\nIf you could visit one place in the world, where would you go?")
    dream_vacation[name] = vacation
    poll = input("Do you want to ask anyone (Yes/ No)")
    if poll == 'No':
        break
for n, v in dream_vacation.items():
    print(f"{n} would like to go {v} for vacation")