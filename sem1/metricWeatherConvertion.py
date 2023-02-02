#start

#calculation functions
def calcTemp(temp):
    return((temp-32)*(5/9))

def calcWind(speed):
    return(speed*1.609)

def calcSnow(inch):
    return(inch*2.54)

#taking info from user
print("Hello!")

FTemp = input('So first, how cold is it right now? (in Fahrenheit)\n')

FMiles = input('and how fast is the wind going right now? (in miles)\n')

FInches = input('and finaly how deep was the snow from the recent snow storm? (in inches) \n')

#printing final results

print("Ok, so the temperature in Celsius is", round(calcTemp(float(FTemp))), "degrees")

print("and the wind speeds in kilometers is about", round(calcWind(float(FMiles)),1), "per hour")

print("and lastly the amount of snow on the ground in centimeters is", round(calcSnow(float(FInches)),1),"CM")

print("thank you")