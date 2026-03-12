cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#----------------------------------------------
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)
print("\n Here is the sorted list:")
print(sorted(cars))
print(sorted(cars, reverse=True))
print("\n Here is the original list again:")
print(cars)
cars.reverse()
print(cars)
print(len(cars))