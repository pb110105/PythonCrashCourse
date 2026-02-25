from pathlib import Path
pathfile10 = Path('10/guest_book.txt')
while True:
    name = input("Please enter your name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break
    else:
        try:
            with pathfile10.open('a') as f:
                f.write(name + '\n')
        except Exception as e:
            print(f"The input should be a string. Please try again")