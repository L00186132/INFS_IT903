#################################################################
#################################################################
# Simle Lists
my_list = [1,2,3,4,"A"]
a = len(my_list)

print(a)
slice_1 = my_list[1:3:1]
print(slice_1)

my_character = my_list[-1]
print(my_character)


# Concatination
my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S","T","Fish",9,10]
concatination_list = my_list_1 + my_list_2
print(concatination_list)

# nested
my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S","T","Fish",9,10]
concatination_list = [my_list_1, my_list_2]
print(concatination_list)

# mutable
my_list_1 = [1,2,3,4,"A"]
print(my_list_1)
my_list_1[2] = "Chips"
print(my_list_1)

# methods
my_list = ["One","Two","Three"]
print(my_list)
my_list.append("Four")
print(my_list)

# String To List
my_string = "12/9/22, 14:30, System Start, UB2204-Server"
list_of_values = my_string.split(",")
print(list_of_values)

#################################################################
#################################################################

# Tuples - immutable
my_list = ["one","two","three"]
my_tuple = ("one","two","three")
print(type(my_list))
print(type(my_tuple))

my_tuple1 = ("one","two","three","one")
#How many times does "one" appear in the tuple
print(my_tuple.count("one"))
# At what position in the tuple can I first fid "one"
print(my_tuple.index("one"))

a = ('Product', '500.00', '1200.00', 'Monkey')
print (a)
a = list(a)
a.insert(3, 'foobar')
a[1] = "kiwi"
a = tuple(a)
print (a)

#################################################################
#################################################################

# Dictionaries
my_dictionary = {"FName":"John", "SName":"ORaw", "Occupation":"Rocket Scientist"}
print(my_dictionary)
print("Works as a " + my_dictionary["Occupation"])
# cannot index or slice a dictionary. 
# Keys must always be strings.

my_dictionary["Salary"] = "Not Enough"
print(my_dictionary)

my_dictionary["Occupation"] = "Brain Surgeon!"
print(my_dictionary)

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

#################################################################
#################################################################
my_set = set()
print(type(my_set))
print(my_set)
my_set.add(1)
my_set.add(2)
my_set.add(2)
print(my_set)

