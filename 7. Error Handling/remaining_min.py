# I have two variables on my diesel backup generator. 
#      fuel in litres 
#      fuel_consumption in litres per minute. 
# I can calculate my remaining endurance in minutes as: Endurance= Fuel/(Fuel Consumption) 
# Whenever the motor is idling, the flowmeter cannot calculate fuel flow and sets it = 0. 
# Write a function to calculate the remaining endurance in minutes, checking and handling for divide by zero errors and for any value errors. 

fule = 145                # liters
fuel_consumption = 3.5    # per min

def remaining_runtime():
  while True:
    try:
      endurance= fule/(fuel_consumption)
    except:
      print("Error")
      continue
    else:
      print(round(endurance,2))
      break
    finally:
      # Continue
      print("This message shows every time, regardless of the programme flow")

remaining_runtime()
