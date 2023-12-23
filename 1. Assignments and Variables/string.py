#Coding with Strings
a = "Greetings!"
print(a[0:4:1])

print(a[-1:-5:-1])

print(a[5])

a = "John"
first_letter = a[0:2:1]
last_letter = a[-1]
insert_letter = "a"
b = last_letter + insert_letter + last_letter
print(b)

first_character = "l"
second_character = "4"
a = first_character + second_character
print(a)

first_number=1
second_nummber = 2
a = first_number + second_nummber
print(a)

# String Interpolation
a="would you like breakfast"
print("Goomd Moerninig" + a)

a=5
b=12
print("Good morning, PMM, For breakfast, would you like {}?".format("Fruit"))
print("We have {}, apples, {} banana's and a total of {} pieces available.".format(a,b,a+b))

a="Good"
b="PMM"
c="Morning"
print("Message is: {first} {third} {second}".format(first=1, second=c, third=b))

Number = 12345
Divisor = 333
Result = Number/Divisor
print("Result of {} divided by {} is {}".format(Number, Divisor, Result))
print("Limiting to a float with 4 decimal places would give {r:1.4f}".format(r=Result))

print(f"Result of {Number} divided by {Divisor} is {Result}")

# Escape Sequences
print("Good Morning PMM")
print("Brekkie")

print("Good Morning PMM", end = " ")
print("Brekkie")

print("Good Morning PMM\nBrekkie")

a="Good Morning, PMM\nWould you like brekkie?"
print(len(a))

my_string = "almost finished now folks!"
my_upper = my_string.upper()
my_lower = my_string.lower()
print(f"Original: {my_string}")
print(f"Upper: {my_upper}")
print(f"Lower: {my_lower}")

test_with_spaces = "     PMM       "
text_without_spaces = test_with_spaces.strip()
print(text_without_spaces)

test_with_brackets = "(PMM)"
text_without_brackets = test_with_brackets.strip('(')
text_without_brackets = text_without_brackets.strip(')')
print(text_without_brackets)
