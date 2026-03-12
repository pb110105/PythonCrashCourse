#Working with Multiple Files
from pathlib import Path
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #Failing silently
        pass
        #print(f"Sorry, the file {filename} does not exist.")
    else:
        #Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
path = Path('10/alice.txt')
count_words(path)
filenames = ['10/alice.txt', '10/siddhartha.txt', '10/moby_dick.txt', '10/little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
