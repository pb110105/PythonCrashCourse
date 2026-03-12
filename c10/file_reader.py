#Reading from a file
#REading the Contents of a file
from pathlib import Path
path = Path('10/pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
#contents = path.read_text().rstrip()
print(contents)
#Realtive and Absolute File Paths
#path = Path('text_files/filename.txt')
#path = Path('C:/Users/username/text_files/filename.txt')
#Accessing a File's Lines
lines = contents.splitlines()
for line in lines:
    print(line)