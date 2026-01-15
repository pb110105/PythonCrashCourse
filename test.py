dream_vacation = {}
while True:
    name = input("\nEnter your name")
    vacation = input("\nIf you could visit one place in the world, where would you go?")
    dream_vacation[name] = vacation
    poll = input("Do you want to ask anyone (Yes/ No)")
    if poll == 'No':
        break
for n, v in dream_vacation.items():
    print(f"{n} would like to go {v} for vacation")