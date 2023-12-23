my_list = [1,2,3,"A",5]
a = len(my_list)
print(a)

slice = my_list[0:1:2]
print (slice)

print (my_list[1:3:1])
print (my_list[0:3:1])
print (my_list[0:1:2])
print (my_list[0::-1])
print (my_list[5::-1])
print (my_list[0:1:2])

print (my_list[-1])
print (my_list[-2])

scailing_factor = my_list[1]
magnitude = my_list[2]
print(scailing_factor*magnitude)
print(f"Value:{scailing_factor*magnitude}")

print('Sensor data...')

data = ''
data_check = data.split(", ")

print(data)

if len(data_check) == 0:
    print('No Sensor data received...')