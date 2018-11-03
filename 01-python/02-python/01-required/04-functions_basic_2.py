# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
def countdown(num):
    return_list=[]
    while num>=0:
        return_list.append(num)
        num -= 1
    return return_list
print(countdown(5))
# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.
def print_and_return(vals):
    print(vals[0])
    return(vals[1])
x = print_and_return([2,4])
print(x)

# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.
def frist_plus_length(vals):
    sum=0
    sum = vals[0] + len(vals)
    print(vals[0])
    print(len(vals))
    return sum
print(frist_plus_length([2,3,4,5,6,7,8,9,10]))

# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the function return False
def values_greater_than_second(vals):
    return_vals = []
    count = 0
    if (len(vals) > 1):
        for value in vals:
            print(value)
            if(value > vals[1]):
                return_vals.append(value)
                count +=1
                print("counts " + str(count))
        return return_vals
    else:
        return False

print(values_greater_than_second([1,2,3,4]))

# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].
def lengthAndValue(size, value):
    return_list=[]
    while size > 0:
        return_list.append(value)
        size -= 1
    return return_list
print(lengthAndValue(4,7))

