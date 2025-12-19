#2.11 Adding Comments
#Full name exercise
first_name = "ada"
last_name = "lovelace"
first_name1 = "pham"
last_name1 = "bao"
first_name2 = "jon"
last_name2 = "doe"
full_name = f"{first_name} {last_name}"
full_name1 = f"{first_name1} {last_name1}"
full_name2 = f"{first_name2} {last_name2}"
message = f"\tHello, {full_name.title()}\n"
message1 = f"\tHello, {full_name1.title()}\n "
message2 = f"\tHello, {full_name2.title()}\n"
print(message)
print(message1)
print(message2)

#####
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print(favorite_language)

###
nostarch_url = 'https://nostarch.com'
level = 'superAMG'
name = "ronaldo calo"
code_game = 'amdGame'
print(code_game.removeprefix('amd'))
print(name.removeprefix('ronaldo'))
print(level.removeprefix('super'))
print(nostarch_url.removeprefix('https://'))