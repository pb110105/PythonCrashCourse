#4-1. Pizzas
pizzas = ['cheese', 'pepperoni', 'vegetarian']
for pizza in pizzas:
    print(f"I love {pizza.title()} pizza.")
print("I really love pizza!\n")
#4-2. Animals
animals = ['dog', 'cat', 'horse']
for animal in animals:
    print(f"A {animal.title()} would make a great pet.")
print("Any of these animals would make a great pet!")
print("\n")
#4-3. Counting to Twenty
for value in range(1,21):
    print(value)

print("\n")
#4-4. One Million
numbers = list(range(1,1000001))
#for number in numbers:
#    print(number)
#4-5. Summing a Million
print(max(numbers))
print(min(numbers))
print(sum(numbers))
#4-6. Odd Numbers
odd_numbers = list(range(1,21,2))
for odd in odd_numbers:
    print(odd)
#4-7. Threes
threes = [value for value in range(3,31,3)]
for three in threes:
    print(three)
#4-8. Cubes
cubes = [value ** 3 for value in range(1,11)]
for cube in cubes:
    print(cube)
#4-9. Cube Comprehension
cubes_comp = [value ** 3 for value in range(1,11)]
for cube in cubes_comp:
    print(cube)
#4-10. Slices
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three players in the list are: ", players[:3])
print("The middle three players in the list are: ", players[1:4])
print("The last three players in the list are: ", players[-3:])
#4-11. My Pizza, Your Pizza
friend_pizzas = pizzas[:]
pizzas.append('bbg')
friend_pizzas.append('chicken')
print("My favorite pizzas are: ")
for i in pizzas:
    print(i)
print("\nMy friend's favorite pizzas are: ")
for i in friend_pizzas:
    print(i)
#4-12.More loops
#4-13. Buffet
buffet = ('sushi', 'steak', 'pizza', 'salad', 'salmon')
for buf in buffet:
    print(buf)
print("\n")
#buffet[0] = 'pasta'
buffet = ('pasta', 'steak', 'pizza', 'lemon', 'salmon')
for buf in buffet:
    print(buf)
