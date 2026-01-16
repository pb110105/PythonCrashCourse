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
