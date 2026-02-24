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


