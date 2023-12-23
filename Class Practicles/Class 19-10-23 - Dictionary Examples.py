"""
By: PMM
Initial: 19OCT23
Prupose: demonstrate Dictionary
"""
my_list = [1,2,3,4,5,6]
print(my_list)

my_dictionary = {"Fuel":"1", "Oil":"2"}
print("Fuel:" + my_dictionary["Fuel"])
print("################################")

my_dictionary2 = {"Fuel":1, "Oil":2}
F = my_dictionary2["Fuel"]
O = my_dictionary2["Oil"]
print(f"Fuel::{F}")
print(f"Oil::{O}")
print("################################")

my_dictionary3 = {"Fuel":"1", "Units":"Ltr"}
F = my_dictionary3["Fuel"]
U = my_dictionary3["Units"]
print(f"Fuel is :{F} in {U}")
print("################################")

my_dictionary4 = {"Fuel":[1,2,3], "Units":"Ltr"}
F = my_dictionary4["Fuel"]
U = my_dictionary4["Units"]
print(f"Fuel is :{F} in {U}")
print("################################")

navData = ["GNGGA",120113.00,5510.0019168,"N"]

#time_in_UTC=(navData[1])
utctime = {"UTC":(navData[1])}
print(utctime)
print("################################")