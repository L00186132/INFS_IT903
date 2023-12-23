# Exercise 1
# Briefly explain and comment this code. 
# What values in the final statement will result in the function returning True? 
# Why?
def divisible(numerator: int, denominator: int)->bool:
    return numerator % denominator == 0

print(divisible(30,4))


# Exercise 2
# Briefly explain and comment this code. 
# Why do you get the value None? 
# What values in the final statement will result in the function returning True? 
# Why? 
# Can you modify this function to return False instead of None if the value is not found?
def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass

result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)


# Exercise 3
# Write a function to search for an even number in a list of numbers. 
# Return True if you find an even number. 
# Return False if you do not. 
# Write a lambda function to calculate the volume of a cylinder.
def even_num(number_list: list, number: int):
    for iterate_number in number_list:
        if iterate_number % number == 0:
            print(f"{iterate_number} is even")
            

even_num([1,2,3,4,5,6,7,8,9,10,11,12,13], 2)
