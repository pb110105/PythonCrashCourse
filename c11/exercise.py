#11-1. City, Country
def city_country(city, country):
    return f"{city}, {country}"
#11-2. Population
def city_country_population(city, country, population):
    return f"{city}, {country} - population {population}"
#11-3. Employee
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    def give_raise(self, raise_amount):
        self.salary = 5000 + raise_amount
        
