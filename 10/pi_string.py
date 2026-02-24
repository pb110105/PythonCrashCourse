#Working with a File's Contents
from pathlib import Path
path = Path('10/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
#for line in lines:
#    pi_string += line
#print(pi_string)
#print(len(pi_string))
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))
#Large Files: One Million Digits
path2 = Path('10/pi_million_digits.txt')
contents2 = path2.read_text()
lines2 = contents2.splitlines()
pi_string2 = ''
for line in lines2:
    pi_string2 += line.lstrip()
print(f"{pi_string2[:52]}...")
print(len(pi_string2))