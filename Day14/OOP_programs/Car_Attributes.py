# Create a class called Car with attributes like make, model, and year.

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = car("Hundai", "Venue", 2024)
car2 = car("Toyota", "Fortuner", 2009)
car3 = car("Honda", "Verna", 2020)

print(car1.make, car1.model, car1.year)
print(car2.make, car2.model, car2.year)
print(car3.make, car3.model, car3.year)
