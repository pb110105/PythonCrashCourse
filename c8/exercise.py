#8-1. Message
def display_message():
    print("I am learning to use funtion in the chapter 8")
display_message()
#8-2. Favorite Book
def favorite_book(title):
    print(f"My favorite book is {title}")
favorite_book('Harry Potter')
#8-3. T-Shirts
def make_shirts(size, content):
    print(f"You choose size:{size} and the content: {content} for this shirt")
make_shirts(3, "I love PhamBao")
make_shirts(content = "I love you baba", size = 11)
#8-4. Large Shirts
def make_shirts(size, content = "I love Python"):
    print(f"You choose size:{size} and the content: {content} for this shirt")
make_shirts(size ="Large")
make_shirts(size = "Medidum")
make_shirts(size = 4, content = "I hate Python")
#8-5. Cities
def describe_city(city, country = "vietnam"):
    print(f"{city.title()} is in the {country.title()}")
describe_city("Sun","Canada")
describe_city("Bien hoa")
describe_city("Seoul", "Korea")
#8-6. City Names
def city_country(city , country):
    place = f"{city},  {country}"
    return place
print(city_country("Bien Hoa", "Dong Nai"))
print(city_country("Seoul", "Korea"))
print(city_country("Lamthai", "Campuchia"))
#8-7. Album
def make_album(name, title, number = None):
    album = {'Artist': name, 'Album': title}
    if number:
        album = {'Artist': name, 'Album': title, 'Number': number}
    else:
        album = {'Artist': name, 'Album': title}
    return album
album1 = make_album("Lucas", "Seen", 3)
album2 = make_album("Ras", "Done")
album3 = make_album("Moc", "Dix" )
print(album1)
print(album2)
print(album3)
#8-8. User Albums
def make_album(name, title, number = None):
    album = {'Artist': name, 'Album': title}
    if number:
        album = {'Artist': name, 'Album': title, 'Number': number}
    else:
        album = {'Artist': name, 'Album': title}
    return album
while True:
    n = input("Enter artist: ")
    if n == 'q':
        break
    t = input("Enter title: ")
    if n == 'q':
        break
    after_album = make_album(n, t)
    print(after_album)
#8-9. Messages
msg = ['Hello', 'Phambao', 'I will become a King of Pirate']
def show_messages(msg):
    for m in msg:
        print(m)
show_messages(msg)
#8-10. Sending Messages
sent_messages = []
def send_messages(msg, sent_messages):
    while msg:
        current_message = msg.pop(0)
        print(f"\nMessage: {current_message}")
        sent_messages.append(current_message)
print(send_messages(msg, sent_messages))
print("----")
print(msg)
print(sent_messages)
#8-11. Archived Messages
print("--")
archive = send_messages(msg[:], sent_messages)
print(sent_messages)
#8-12. Sandwiches
def make_sandwich(number_of_gredient):
    number_of_gredient = int(number_of_gredient)
    gredients =['potato', 'cheese', 'meet', 'soft', 'tomato', 'chicken']
    sandwich = []
    for i in range(number_of_gredient):
        print(f"Adding {gredients[i].title()} for your sandwich")
        sandwich.append(gredients[i])
    print(f"Your sand wich have {sandwich}")
make_sandwich(4)
make_sandwich(3)
make_sandwich(1)
#8-13. User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Bao', 'Pham', location = 'Bien Hoa', field = 'Data Engineer', date = 2005)
print(user_profile)
#8-14. Cars
def make_car(producer, model, **info):
    info['name_producer'] = producer
    info['name_model'] = model
    return info
car = make_car('subaru', 'outblack', color = 'red', height = 85.3, born = 2004)
print(car)
#8-15. Printing Models
import printing_models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_models.print_models(unprinted_designs, completed_models )
printing_models.show_completed_models(completed_models)
#8-16. Imports
import person
musician = person.build_person('jimi', 'hendrix', age = 17)
print(musician)
from person import build_person
musician = build_person('jimi', 'hendrix', age = 17)
print(musician)
from person import build_person as bp
musiciiian = bp('jimi', 'hendrix', age = 17)
print(musician)
import person as p
musician = p.build_person('jimi', 'hendrix', age = 17)
print(musician)
from person import *
musician = build_person('jimi', 'hendrix', age = 17)
print(musician)
#8-17. Styling Funtions
#Nothing to do in this file