#start

#calculation function to convert and return all the types of information based on the function's arguments
def calculateData(dataType, data):
    if(dataType == 1):
        #calculate temperature
        return str(round((data-32)*(5/9),0))
    if(dataType == 2):
        #calculate wind speeds
        return str(round(data*1.609,2))
    if(dataType == 3):
        #calculate snowfall
        return str(round(data*2.54,2))

#a function to gather data from the user and print the results, this calls the other function to calculate the user input
def gatherAndShowData(option):
    if(option == 1):
        Temp = input('ok, how cold is it right now? (in Fahrenheit)\n')
        print("Ok, so the temperature in Celsius is" + calculateData(1,float(Temp)), "degrees")
    elif(option == 2):
        Miles = input('ok, how fast is the wind going right now? (in miles)\n')
        print("So the wind speeds in kilometers is about", calculateData(2,float(Miles)), "per hour")
    elif(option == 3):
        Inches = input('ok, how deep was the snow from the recent snow storm? (in inches) \n')
        print("The amount of snow on the ground in centimeters is", calculateData(3,float(Inches)),"CM")
    else:
        print("program expected you to type 1, 2, or 3")

#start main code
print("Hello! this program is designed to help convert units of measurement for weather from Fahrenheit to Celsius or imperial to metric!")
print("First what are you trying to convert? option 1: temperature, option 2: windspeed, option 3: snowfall")

#Try and except to make sure the user inputed a int but the else in the function makes sure its a 1 2 or 3
optionInput = input('please type the number of the option you would like to select\n')
try:
    selectedOption = float(optionInput)
except:
    print("the program expects you to type the numbers 1, 2, or 3")
    exit()
#calling fuction
gatherAndShowData(float(selectedOption))
print("Thank you!")
#End