# As part of this assignment, please create a function randInt() where

import random

# randInt() returns a random integer between 0 to 100
def randInt():
    x= int(random.random() * 100)
    print(x)
randInt()


# randInt(max=50) returns a random integer between 0 to 50
def randInt2():
    x = int(random.random()*50)
    print(x)
randInt2()
# randInt(min=50) returns a random integer between 50 to 100
def randInt3(min = 50):
    y=0
    while y >= min:
        y= int(random.random *100)
        return y
print(randInt3())

# randInt(min=50, max=500) returns a random integer between 50 and 500
def randInt4(min=50, max=500):
    x=0
    while x>=min & x<=max:
        x=int(random.random() * max)
    return x 
print(randInt4())
