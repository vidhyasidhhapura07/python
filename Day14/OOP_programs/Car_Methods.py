# Write methods in the class to display the car’s details.

class car:
    def __init__(self, Brand, Name, Year, Price):
        self.Brand = Brand
        self.Name = Name
        self.Year = Year
        self.Price = Price

    def details(self):
        print("Car Details")
        print("Brand :" , self.Brand)
        print("Name : " , self.Name)
        print("Year : ", self.Year)
        print("Price : ", self.Price)

Cars = car("Hundai", "Venue", 2019, "8 Lakh" )
Cars.details()