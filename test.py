#10-14. Veryfi User
import json
from pathlib import Path
path = Path('10/username.json')
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