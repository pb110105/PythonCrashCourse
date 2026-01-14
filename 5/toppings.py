requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
requested_toppings = ['mushrooms', 'extra cheese', 'onions', 'pineapple']
'mushrooms' in requested_toppings
for requested_toppings in requested_toppings:
    if requested_toppings == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_toppings}")
print("\n Finished making your pizza!")
#Checking that a list is not empty
requested_toppings = []
if requested_toppings: 
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\n Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")
print("\n Finished making your pizza!")