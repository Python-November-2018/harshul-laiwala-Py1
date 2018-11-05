# Create a class called  Car. In the __init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

class Car:
    def __init__(self, price=0, speed=0, fuel=0, mileage=0, tax=0):
        self.Price = price
        self.Speed = speed
        self.Fuel = fuel
        self.Mileage = mileage
        self.Tax= self.getTaxRate(price)
        self.display_all()

    def getTaxRate(self, price):
        if price > 10000:
            return 0.15 
        else:
            return 0.12
    def display_all(self):
        temp = vars(self)
        for key in temp:
            print(key+":", temp[key])
        print("\n")
        return self

# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12
car1 = Car(price=2000, speed='35mph', fuel='Full', mileage='15mpg')
# Price: 2000
# Speed: 5mph
# Fuel: Not Full
# Mileage: 105mpg
# Tax: 0.12
car2=Car(price=2000, speed='5mph', fuel='Not Full', mileage='105mpg')
# Price: 2000
# Speed: 15mph
# Fuel: Kind of Full
# Mileage: 95mpg
# Tax: 0.12
car3=Car(price=2000, speed='15mph', fuel='Kind of Full', mileage='95mpg')
# Price: 2000
# Speed: 25mph
# Fuel: Full
# Mileage: 25mpg
# Tax: 0.12
car4=Car(price=2000, speed='25mph', fuel='Full', mileage='25mpg')
# Price: 2000
# Speed: 45mph
# Fuel: Empty
# Mileage: 25mpg
# Tax: 0.12
car5=Car(price=2000, speed='45mph', fuel='Empty', mileage='25mpg')
# Price: 20000000
# Speed: 35mph
# Fuel: Empty
# Mileage: 15mpg
# Tax: 0.15
car6=Car(price=20000000, speed='35mph', fuel='Empty', mileage='15mpg')
