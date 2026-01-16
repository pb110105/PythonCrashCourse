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
