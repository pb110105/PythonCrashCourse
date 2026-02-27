#Saving and Reading User-Generated Data
from pathlib import Path
import json
username = input("What is your name? ")
path = Path('10/username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We will remember you when you come back, {username}!")