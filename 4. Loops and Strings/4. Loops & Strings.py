#################################################################
#################################################################
#If, Elif and Else
a = True
b = True
c = True

if a:
    print("a was true")
elif b:
    print("b was true")
elif c:
    print("c was true")
else:
    print("None of our boolean variables were true")


if (3<2) and (5<9):
    print("Yup!")
else:
    print("Nope!")

#################################################################
#################################################################
# Loops
iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    if item %2 != 0:
        print(item)


iterable_variable = [1,2,3,4,5,6]
total = 0

for item in iterable_variable:
    total = total + item

print(total)


# Define a string to iterate over
for this_letter in "John ORaw":
    # Specify which letter to test for
    if this_letter == "J":
        # Found the test letter
        print(f"Woo hoo, found a {this_letter}!")
        # Exit the current loop
        break
    else:
        # Didn't find the test letter
        print(f"Aww man, I didn't want a {this_letter}!")



my_list = [1,2,3,0]

for my_number in my_list:
    if my_number == 1:
        pass
    if my_number == 2:
        continue
    if my_number == 3:
        print(f"Found the number {my_number}")
    if my_number == 0:
        break



list_of_tuples = [(1,2), (3,4), ("A", "B")]
for item in list_of_tuples:
    print(item)  



# Tuple unpacking
list_of_tuples = [(1,2), (3,4), ("A", "B")]
for a,b in list_of_tuples:
    print(a)  
    print(b)



#################################################################
#################################################################
# While Loops
x = 0
while x < 10:
    print(f"X is = {x}")
    x = x + 1
else:
    print(f"As x is now = {x}, we are all finished")

print("press [ctrl][c] to exit")
#while 1:
#    pass


#################################################################
#################################################################
# List Comprehensions
my_list = []
my_string = "Morning Folks!"
for letter in my_string:
    my_list.append(letter)

print(my_list)


my_string = "Morning Folks!"
my_list = [letter for letter in my_string]
print(my_list)

my_list = [number for number in range(0,20)]
print(my_list)

my_list = [number * 10 for number in range(0,20)]
print(my_list)

my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)

# list of depths in feet on a US Sonar log file, convert them to meters, rounded to 2 decimal places.
conversion = 0.3048
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
my_depth_in_meters = [(round(depth * conversion, 2)) for depth in my_depth_in_feet] 
print(my_depth_in_meters)


