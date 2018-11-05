# Which methods can return self in order to allow chaining methods?
# All class methods can return self 

# Create a new class called Bike with the following properties/attributes:
# price
# max_speed
# miles
class Bike:
    def __init__(self, price=0,max_speed=0):
        self.Price = price
        self.MaxSpeed = max_speed
        self.Miles = 0

# Add the following methods to this class:
## displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
## ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
## reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...        
    def display_info(self):
        print("Max Speed is {},\n Price of the Bike is {}\n dollars Miles travelled is {} \n".format(self.MaxSpeed , self.Price , self.Miles))
        return self
    def ride(self):
        print("Riding")
        self.Miles += 10
        return self
    # What would you do to prevent the instance from having negative miles?
    def reversing(self):
        if self.Miles > 0:
            print("Reversing")
            self.Miles -= 5
            return self
        else:
            print("Bike has travelled 0 miles an cannot reverse. Please ride before reversing")
            return self

# Create 3 instances of the Bike class.
## Use the __init__() method to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__(), also write the code so that the initial miles is set to be 0 whenever a new instance is created.

bike1 = Bike(200, max_speed="25mph")

bike2 = Bike(price=250,max_speed="30mph")

bike3 = Bike(price=250, max_speed="30mph")
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
bike1.ride().ride().ride().reversing().display_info()
bike2.ride().ride().reversing().reversing().display_info()
bike3.reversing().reversing().reversing().display_info()