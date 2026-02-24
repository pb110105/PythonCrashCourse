import sys
print("1. Starting...", flush=True)
name = input("Please enter your name: ")
with open('test_debug.txt', 'w') as f:
    f.write(f"Name: {name}\n")
print("2. Done!", flush=True)