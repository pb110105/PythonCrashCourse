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
#5-10. Guest Book
from pathlib import Path
pathfile10 = Path('10/guest_book.txt')
while True:
    name = input("Please enter your name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break
    with pathfile10.open('a') as f:
        f.write(name + '\n')
