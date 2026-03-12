#Defining function
def greeter_user():
    """Display simple greeting"""
    print("Hello!")
greeter_user()
#Passing information to a Fusion
def greeter_user(username):
    """"Display a simple  greeting"""
    print(f"\nHello, {username.title()}")
greeter_user('Bao')
#Arguments and Parameters
#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name
#This is an infinite loop!
while True:
    print("\nPlease tell me your name: ")
    print("\nEnter 'q' to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}")