# Basic - Print all the numbers/integers from 0 to 150.
def basic():
    for i in range(151):
        print(i)
basic()
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
def Multiples_of_Five():
    for i in range(5,1000000):
        if i%5==0:
            print(i)

Multiples_of_Five()

# Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
def CountingDojoWay():
        for i in range(101):
                if i%5==0:
                        print("Coding"+str(i))
                        if i%10==0:
                                print("Coding Dojo"+str(i))
CountingDojoWay()
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def Suckers_huge():
        sum=0
        for i in range(0,500001,1):
                sum = sum+i
        return sum
x= Suckers_huge()
print(x)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
def Countdown_By_Fours():
    x=2018
    while x>0:
        print(x)
        x=x-4
Countdown_By_Fours()

# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
def felxible_count(low_num, high_num,mult):
    for i in range(low_num, high_num):
        if i % mult ==0:
            print(i)
felxible_count(2,9,3)