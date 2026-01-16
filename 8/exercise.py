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
