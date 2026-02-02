# Create a subclass ElectricCar that inherits from Car and adds an additional battery_size attribute.

class Cars:
    def __init__(self, make, model, year):
        self.model = model
        self.year = year
        self.make = make

    def details(self):
        print(f"cars:  {self.model} {self.make} {self.year}")

class ElectricCar(Cars):
    def __init__(self, make, model, year, battery_size):

        super().__init__(make, model, year)
        self.battery_size = battery_size

    def details(self):
        super().details()
        print(f"Battery Size: {self.battery_size} kWh")

my_electric_car = ElectricCar("Tesla", "Model 3", 2024, 75)
my_electric_car.details()
