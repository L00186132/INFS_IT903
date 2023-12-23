from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)

weekday = dt.now().strftime("%A") 
print(weekday)

month = dt.now().strftime("%B")
print(month)

#Add to the code above and print human readable values for current time (hours, minutes, seconds) and date (year, month, day).
print("(", today.strftime("%H:%M:%S"), ")", "(", today.strftime("%Y, %m, %d"), ")")
