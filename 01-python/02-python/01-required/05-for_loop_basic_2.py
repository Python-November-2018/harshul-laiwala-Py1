# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def makeItBig(vals):
    for index in range(len(vals)):
        if vals[index] > 0:
            vals[index] = "Big"
    return vals
print(makeItBig([-1, 3, 5, -5]))

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def countPositives(vals):
    countPositives = 0
    for index in range(len(vals)):
        if vals[index] > 0:
            countPositives +=1
    vals[len(vals)-1] = countPositives
    return vals
print(countPositives([-1,1,1,1]))

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal(vals):
    sum=0
    for index in range(len(vals)):
        sum += vals[index]
    return sum
print(sumTotal([1,2,3,4]))


# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def multiples(vals):
    sum=0
    avg=0
    for index in range(len(vals)):
        sum += vals[index]
    avg = sum/len(vals)
    return avg
print(multiples([1,2,3,4]))

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def length(vals):
    return len(vals)
print(length([1,2,3,4]))

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum(vals):
    minimum = vals[0]
    for index in range(len(vals)):
        if vals[index] < minimum:
            minimum = vals[index]
    return minimum
print(minimum([-1,-2,-3]))
print(minimum([1,2,3,4]))

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def maximum(vals):
    maximum = vals[0]
    for index in range(len(vals)):
        if vals[index] > maximum:
            maximum = vals[index]
    return maximum
print(maximum([-1,-2,-3]))
print(maximum([1,2,3,4]))

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
# def UltimateAnalyze(vals):
#     return_dict = {
#         "avg"= 0
#         "maximum"=vals[0]
#         "minimum"=vals[0]
#         "sum"=0
#         length = len(vals)
#     }
#     for index in range(length):
#         sum += vals[index]
#         if vals[index] < minimum:
#             minimum = vals[index]
#         elif vals[index] > maximum:
#             vals[index] = maximum
#     avg = sum/length
#     return return_dict
    
# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverse(vals):
    return vals.reverse()
print(reverse([1,2,3,4]))

