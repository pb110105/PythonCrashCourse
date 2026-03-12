#Filling a Dictionary with User Input
responses = {}
#Set a flag to indicate that polling is active
polling_active = True
while polling_active:
    #Prompt for the person's name and response
    name = input("What is your name?")
    response = input("Which mountain would you like to climb someday?")
    #Store the reponse in the dictionary
    responses[name] = response
    #Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respone? (Yes/ No)")
    if repeat == 'No':
        polling_active = False
#Polling is complete. Show the Results
print("\n--Poll Results--")
for name, response in responses.items():
    print(f"{name} would like to climn {response}")
