#2-3.Personal Message
name = "Barry"
print(f"Hello {name}, would you like to learn some Python today?")
#2-4.Name Cases
print(name.lower())
print(name.upper())
print(name.title())
#2-5. Famouse Quote
famous_person = "Albert Einstein"
quote = '"A person who never made a mistake never tried anything new."'
print(f'{famous_person} once said, {quote}')
#2-6. Famous Quote 2
message = f'{famous_person} once said, {quote}'
print(message)
#2-7. Stripping Names
stripping_name = " \tBarry\n "
print(stripping_name)
print(stripping_name.lstrip())
print(stripping_name.rstrip())
print(stripping_name.strip())
#2-8. File Extensions
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))