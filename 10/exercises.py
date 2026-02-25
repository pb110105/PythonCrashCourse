#10-1. Learning Python
from pathlib import Path
path_learning_python = Path('10/learning_python.txt')
contents_lp = path_learning_python.read_text()
print(contents_lp)
list_lp = contents_lp.splitlines()
print(list_lp)
#10-2. Learning C.
contents_lp_replace = contents_lp.replace('Python', 'C')
print(contents_lp_replace)
#10-3. Simpler Code
from file_reader import path, contents, lines
for line in contents.splitlines():
    print(line)
#10-4. Guest
name = input("Please enter your name: ")
pathfile = Path('10/guest.txt')
pathfile.write_text(name)
#10-5. Guest Book
from pathlib import Path
pathfile10 = Path('10/guest_book.txt')
while True:
    name = input("Please enter your name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break
    with pathfile10.open('a') as f:
        f.write(name + '\n')
#10-6. Addition 
while True:
    result = 0
    number1 = input("Enter the first number (or 'quit' to exti): ")
    if number1.lower() == 'quit':
        break
    number2 = input("Enter the second number (or 'quit' to exit): ")
    if number2.lower() == 'quit':
        break
    else:
        try:
            result = int(number1) + int(number2)
            print(f"The sum of {number1} and {number2} is: {result}")
        except ValueError:
            print("The value shoud be a number. Please try again")
#10-7. Addition Calculator
from pathlib import Path
pathfile10 = Path('10/guest_book.txt')
while True:
    try:
        name = input("Please enter your name (or 'quit' to exit): ")
        if name.lower() == 'quit':
            break
        with pathfile10.open('a') as f:
            f.write(name + '\n')
    except Exception as e:
        print(f"The input should be a string and it is an English name. Please try again")
#10-8. Cats and Dogs
catPath = Path('10/cats.txt')
dogPath = Path('dogs.txt')
try:
    contents_cat = catPath.read_text()
    print(contents_cat)
    contents_dog = dogPath.read_text()
    print(contents_dog)
except FileNotFoundError:
    print("One of Files not found")
#10-9. Silent Cats and Dogs
from pathlib import Path
catPath = Path('10/cats.txt')
dogPath = Path('dogs.txt')
try:
    contents_cat = catPath.read_text()
    print(contents_cat)
    contents_dog = dogPath.read_text()
    print(contents_dog)
except FileNotFoundError:
    pass
#10-10. Common words
path_common_words = Path('10/siddhartha.txt')
common_words = path_common_words.read_text(encoding='utf-8')
print(common_words.count('the'))
print(common_words.lower().count('the'))
