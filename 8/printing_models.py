#Modifying a List in a Function
#Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
#Stimulate printting each design , until none are left
#Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
#Display all completed design
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    """Stimulate printing each design, until none are left
    Move each design to completed_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe followiing models have been printing")
    for completed_model in completed_models:
        print(completed_model)
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)