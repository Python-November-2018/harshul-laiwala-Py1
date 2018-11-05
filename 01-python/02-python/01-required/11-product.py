# Product Class:
# Attributes:

# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
class Product:
    def __init__(self, brand, price=0, weight=0, status="For Sale"):
        self.Price= price
        self.Weight = weight
        self.Brand = brand
        self.Status = status
    
# Methods:

# Sell: changes status to "sold"
    def sell(self):
        self.Status = "Sold"
        return self
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def add_tax(self, taxrate = 0.0):
        if self.Price > 0:
            self.Price = self.Price * taxrate
        else: print("The price is 0. Please add a price for the product")
        return self
            
# Return Item: takes reason_for_return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
    def return_items(self, reason_for_return):
        if reason_for_return == 'defective':
            self.Status = reason_for_return
            self.Price = 0
            return self
        elif reason_for_return == 'like_new':
            self.Status = 'For Sale'
            return self
        elif reason_for_return == 'opened':
            self.Status = 'Used'
            self.Price = self.Price * 0.2
            return self
        else:
            print("Not a valid Reason for Return")
            return self


# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.
    def display_all(self):
        temp = vars(self)
        for key in temp:
            print(key+":", temp[key])
        print("\n")
        return self