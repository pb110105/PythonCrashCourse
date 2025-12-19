motorcycles = ['honda', 'yamada', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('nanami')
print(motorcycles)
#----------------------------------------------
motorcycle = []
motorcycle.append('suzuki')
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('bmw')
print(motorcycle)
#----------------------------------------------
motorcycles.insert(0, 'bmw')
motorcycles.insert(2, 'mecedes')
print(motorcycles)
#----------------------------------------------
del motorcycles[1]
del motorcycles[0]
print(motorcycles)
#----------------------------------------------
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#----------------------------------------------
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")
#----------------------------------------------
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned wwas a {first_owned.title()}")
print(motorcycles)
#----------------------------------------------
motorcycles.append('honda' )
motorcycles.append('toyota')
motorcycles.append('suzuki')
motorcycles.append('mecedes')
print(motorcycles)
motorcycles.remove('toyota')
print(motorcycles)
#----------------------------------------------
too_expensive = 'mecedes'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")
#----------------------------------------------
print(motorcycles)
#print(motorcycles[3])
print(motorcycles[-1])
