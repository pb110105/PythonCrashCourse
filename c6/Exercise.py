#6-1. Person
person = {
    'first_name': 'Anh',
    'last_name': 'Nguyen',
    'age': 17,
    'city': 'Bien Hoa'
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
#6-2. Favorite Numbers
favorite_numbers = {
    'Hung': 7,
    'Anh': 8,
    'Bao': 1,
    'Nha': 3,
    'Nhi': 45
}
print("Hung: " + str(favorite_numbers['Hung']))
print("Anh: " + str(favorite_numbers['Anh']))
print("Bao: " + str(favorite_numbers['Bao']))
print("Nha: "+ str(favorite_numbers['Nha']))
print("Nhi: " + str(favorite_numbers['Nhi']))
#6-3. Glossary
glossary = {
    'string': 'A series of characters.',
    'list': 'A collection of times in a particular order.',
    'dictionary': 'A collection of key-value pairs',
    'loop': 'A way to repeat code multiple times.',
    'function': 'A block of code that performs a specific task.'
}
print("string: " + glossary['string'])
print("list: " + glossary['list'])
print("dictionary: " + glossary['dictionary'])
print("loop: " + glossary['loop'])
print("function: " + glossary['function'])
print("\n")
#6-4. Glossary 2
for w, d in glossary.items():
    print(f"{w.title()}: {d}")
#6-5. Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}
for r, c in rivers.items():
    print(f"The {r.title()} runs through {c.title()}")
for r in rivers.keys():
    print(r.title())
for c in rivers.values():
    print(c.title())
#6-6. Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
people = ['jen', 'phil', 'bao', 'hung']
for p in people:
    if p in favorite_languages.keys():
        print(f"Thank you for taking the poll, {p.title()}")
    else:
        print(f"Hey {p.title()}, please take our poll!")
#6-7. People
people = {
    'bao': {
        'first_name': 'Pham',
        'last_name': 'Bao',
        'age': 21,
        'city': 'Hanoi',
    },
    'anh': {
        'first_name': 'Nguyen',
        'last_name': 'Anh',
        'age': 17,
        'city': 'Bien Hoa',
    },
    'hung': {
        'first_name': 'Nguyen',
        'last_name': 'Hung',
        'age': 20,
        'city': 'HCM',
    }
}
for u, ins in people.items():
    print(f"\nUsername: {u.title()}")
    full_name = f"{ins['first_name']} {ins['last_name']}"
    age = ins['age']
    city = ins['city']
    print(f"\tFull name: {full_name}, age: {age}, city: {city}")
#6-8. Pets
Dog = {
        'kind': 'Corgi',
        'owner': 'Bao',
    }
Cat = {
        'kind': 'Siamese',
        'owner': 'Anh',
    }
Pets = [Dog, Cat]
for p in Pets:
    print(f"\nKind: {p['kind']}")
    print(f"\nOwner: {p['owner']}")
#6-9. Favorite Places
favorite_places = {
    'bao': ['hanoi', 'danang', 'saigon'],
    'anh': ['bienhoa', 'dalat'],
    'hung': ['hcm', 'cantho', 'vungtau'],
}
for n, ps in favorite_places.items():
    print(f"\n{n.title()}'s favorite places are: ")
    for p in ps:
        print(f"\t{p.title()}")
#6-10. Favorite Numbers
favorite_numbers = {
    'bao': [3, 7, 9],
    'anh': [8, 10],
    'hung': [1,3,2],
}
for n, num in favorite_numbers.items():
    print(f"\n{n.title()}'s favorite numbers are: ")
    for n in num:
        print(f"\t{n}")
#6-11. Cities
cities = {
    'HCM': {
        'country': 'vietnam',
        'population': 9000000,
        'fact': 'the biggest city in vietnam',
    },
    'paris': {
        'country': 'france',
        'population': 2000000,
        'fact': 'the city of love',
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'the capital of japan',
    },
}
for c , info in cities.items():
    print(f"\nCity: {c.title()}")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")
#6-12. Extensions
#(no code needed for this exercise)
# --- IGNORE ---
#This file is to ignore the warning of empty file in the 6th chapter's folder
