#################################################################
#################################################################
# Errors

# Better coding practice to import specific function you require from a module, 
# allows function to be directly accessed within your code. 
from math import sin, cos, radians


# Take an input number as a string and convert it to an integer
my_value = int(input("Enter an integer greater than 0"))

if my_value <= 0:
    raise Exception("Values must be > 0")
else:
    print("Validation checks passed")
