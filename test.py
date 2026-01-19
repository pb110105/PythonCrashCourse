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
