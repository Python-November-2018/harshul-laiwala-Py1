# Assignment: MathDojo
# Objectives:
# Practice creating a class and creating new instances
# Practice chaining methods
# Practice writing flexible functions that can take a variable number of arguments
# HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
class MathDojo:
    def __init__(self):
        self.Result =0
    
    def add(self, *values ):
        for value in values:
            self.Result += value
            print("result of add:{}",format(self.Result))
            return self 
    def subtract(self, *values):
        for value in values:
            self.Result -= value
            print("result of subtract:{}",format(self.Result))
            return self
    def result(self):
        print("final result:{}",format(self.Result))
        return self.Result
        
# Then create a new instance called md. It should be able to do the following task:
md=MathDojo()
x=md.add(2).add(2,5,1).subtract(3,2).result()
print(x) # should print 5
# which should perform 0+2+(2+5+1)-(3+2) and print 5.