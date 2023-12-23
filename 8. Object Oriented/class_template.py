"""
Class template by PMM

Revision History
06OCT22: Alpha
11OCT23: Beta
"""

class Demo_Template():
    # class object attribute,
    class_object_attribute1 = 123
    
    # Default Constructor
    def __init__(self) -> None:
        print("Constructor 1 ran")
        
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor 2 ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")


# Instantiate the class
#my_object_1 = MyTemplate()
#print(type(my_object_1))

# Instantiate the class
my_object = Demo_Template("Yoda", True)
print(type(my_object))

# Check the object
print(my_object.class_object_attribute1)

my_object.my_method1()
my_object.my_method1('Yoda')
                     