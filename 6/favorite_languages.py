#A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")
for n, l in favorite_languages.items():
    print(f"{n.title()}'s favorite language is {l.title()}")
#Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())
for name in favorite_languages.values():
    print(name.title())
for name in favorite_languages:
    print(name.title())
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
