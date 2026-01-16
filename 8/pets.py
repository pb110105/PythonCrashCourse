#Passing Arguments
#Position Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet('Dog', 'Ronaldo')
#Multiple function Calls
describe_pet('Cat', 'Chihuahua')
describe_pet('Hamster', 'San')
#Order Matters in Positional Arguments
describe_pet('San', 'Hamster')
#Keyword Arguments
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(pet_name = 'hary', animal_type = 'hamster')
#Default Values
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(pet_name = 'willie')
#Equivalent Function calls
#A dog named willie
describe_pet('willie')
describe_pet(pet_name = 'willie')
#A hamster named harry
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')
#Avoiding Argument Errors
describe_pet()