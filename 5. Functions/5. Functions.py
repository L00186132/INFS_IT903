#################################################################
#################################################################
#Anatomy
def name_of_function(first_name):
    """
    Simple test function
    """
    print(f"Yoo hoo, hello {first_name}!")

name_of_function("JOR")



#################################################################
#################################################################
# # Passing and returning values
def calculate_circumference(radius):
    """
    Calculate the circumference of a circle based on its radius
    """
    return 2 * 3.142 * radius 

a = calculate_circumference(5)
print(a)


def calculate_circumference(radius):
    """
    Calculate the circumference of a circle based on its radius

    """
    return 2 * 3.142 * radius 


#r = input("Provide a radius value: ")
#r_float = float(r)
#a = calculate_circumference(r_float)
#print(a)


def auto_adder(*my_numbers):
    final_number = 0
    for number in my_numbers:
        final_number = final_number + number
    final_number = sum(my_numbers)

    return final_number

print(auto_adder(12,34,23,66,8,99))



#################################################################
#################################################################
# Type Hints - I could tell function that I am passing a float and expect it to return a float.
#def calculate_circumference(radius: float) -> float:




#################################################################
#################################################################
# Tuple Unpacking
def most_expensive(price_list):
    """
    Iterate through a list and find the most expensive item
    """
    # Set up the variables
    max_price = 0
    max_price_item = ""
    # Iterate, unpacking the tuple
    for description, price in price_list:
        # If this is the maximum price, record that in our variables
        if price > max_price:
            max_price = price
            max_price_item = description
        # If it is not the maximum price, do nothing
        else:
            pass
    # Return the maximum prices item and its price
    return max_price_item, max_price

# Provide the data
price_list = [("Pineapple", 1.0,), ("Apples", .5), ("Pears", .7), ("Peaches", .8)]
# Call the function and unpack its return values
product, price  = most_expensive(price_list)
print(product, price)



#################################################################
#################################################################
# Map and Lambda
def double_number(n: int)->int:
    """
    Simple function to double a number
    """
    return n+n

# Create a list of numbers for testing
my_numbers = [1,2,3,4,5]
# Map my_numbers to the double_number function, return type is map
result = map(double_number, my_numbers)
# Print a list of the map 
print(list(result))
# Or iterate through it
for item in map(double_number, my_numbers):
    print(item)



circumference = lambda radius : 2 * 3.142 * radius
area = lambda radius : 3.142 * radius * radius
radius = 5
print(circumference(radius), area(radius))



#################################################################
#################################################################
# Scope
my_string = "global"

def my_function():
    my_string = "enclosing"
    def nested_function():
        my_string = "local"
        print(my_string)
    nested_function()
    return my_string

# Print the variable my_string
print(my_string)
# Print the output of the function, my_function
print(my_function())


my_string = "global"

def my_function():
    global my_string
    print(f"At the moment, my_string is: {my_string}")
    my_string = "mangled!"

my_function()
print(f"Now the global value of my_string is: {my_string}")












