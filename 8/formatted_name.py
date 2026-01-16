#Return Values
#Return a Simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musican = get_formatted_name('jimi', 'hendrix')
print(musican)
#Making an Argument Optional
def get_formatted_name(first_name, last_name , middle_name = " "):
    """Return full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
muscian = get_formatted_name("jimi" , "hendrix")
print(musican)
musican = get_formatted_name("Pham", "Tran", "Quoc Bao")
print(musican)