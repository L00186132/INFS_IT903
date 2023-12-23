#Exercises:
conversion = 273.15

kelvin  = [273.15,300.22,640.44,132.12,553.23,666.88,987.56,3464.77,23.33,6.0,0]
celsius = [(round(kel - conversion, 2)) for kel in kelvin] 
print(celsius)