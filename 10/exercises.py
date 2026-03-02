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
#10-11. Favorite number
from pathlib import Path
import json
favorite_path = Path('10/favorite_number.json')
def input_favorite_number():
    number  = int(input("What is your favorite number?"))
    contents = json.dumps(number)
    favorite_path.write_text(contents)
def show_favorite_number():
    if favorite_path.exists():
        contents = favorite_path.read_text()
        number = json.loads(contents)
        print(f"I know your favorite number. That is {number}")
    else:
        input_favorite_number()
show_favorite_number()
#10-12. Favorite number remembered
from pathlib import Path
import json
uf_path = Path('10/favorite_number.json')
def input_favorite_number():
    """Prompt user favorite number"""
    try:
        number = int(input("What is your favorite number?"))
        contents = json.dumps(number)
        uf_path.write_text(contents)
        return number
    except ValueError:
        print("The value should be a number. Please try again.")
        return None
def get_favorite_number():
    if uf_path.exists():
        contents = uf_path.read_text()
        number = json.loads(contents)
        print(f"I know your favorite number. That is {number}")
    else:
        number = input_favorite_number()
        if number is not None:
            print(f"We will remember your favorite number {number} for next time.")
get_favorite_number()
#10-13. User Dictionary
#10-13. User Dictionary
import json
from pathlib import Path
path = Path('10/user_dict.json')
def get_stored_username():
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict['username'], user_dict['sex']
    else:
        return None, None
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    return username
def get_sex():
    sex = input("What is your sex? ")
    return sex
def dictionary_user():
    username = get_new_username()
    sex = get_sex()
    user_dict = {
        'username': username,
        'sex': sex
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
def greet_user():
    """Greet the user by name."""
    username, sex = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
        print(f"Your sex is {sex}.")
    else:
        dictionary_user()
        print(f"We will remember you when you come back, {username}!")
        print(f"We will remember your sex {sex} for next time.")
greet_user()
#10-14. Verify User
def check_user():
    usernameLogin = input("Hello! Please type your username: ")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        if usernameLogin.lower() == username.lower():
            print(f"Welcome back, {usernameLogin}")
        else:
            print("Username not found. Please register first.")
    else:
        print("Username not found. Please register first.")
check_user()