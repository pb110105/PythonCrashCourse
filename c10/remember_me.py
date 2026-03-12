#Saving and Reading User-Generated Data
from pathlib import Path
import json
#username = input("What is your name? ")
path = Path('10/username.json')
#contents = json.dumps(username)
#path.write_text(contents)
#print(f"We will remember you when you come back, {username}!")
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We will remember you when you come back, {username}!")
#Refactoring
def get_stored_username():
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
def greet_user():
    """Greet the user by name."""
    path = Path('10/username.json')
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We will remember you when you come back, {username}!")
greet_user()
