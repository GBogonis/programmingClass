#start

#calculation function to convert and return all the types of information based on the function's arguments
def calculateData(dataType, data):
    #this function returns the results as a string including the whole answer not just returning a number
    if(dataType == 1):
        #calculate temperature
        return "Ok, so the temperature in Celsius is " + str(round((data-32)*(5/9),0)) + " degrees"
    if(dataType == 2):
        #calculate wind speeds
        return "So the wind speeds in kilometers is about " + str(round(data*1.609,2)) + " per hour"
    if(dataType == 3):
        #calculate snowfall
        return "The amount of snow on the ground in centimeters is " + str(round(data*2.54,2)) + " CM"

#a function to gather data from the user and print the results, this calls the other function to calculate the user input
def gatherAndShowData():
    print("First what are you trying to convert? option 1: temperature, option 2: windspeed, option 3: snowfall")
    
    #Try and except to make sure the user inputed a float and a if to make sure its a 1, 2, or 3
    #the try and except is in a while true loop to let the user try again as many times as they need
    while True:
        option = input('please type the number of the option you would like to select\n')
        try:
            option = float(option)
            if(option == 1 or option == 2 or option == 3):
                break
            print("program expected you to type 1, 2, or 3")
        except:
            print("the program expects you to type the numbers 1, 2, or 3")
 
    #try and excepts after every prompt to make sure the user inputed a good value and a while true loop to give user mamy atempts
    if(option == 1):
        while True:
            Temp = input('ok, how cold is it right now? (in Fahrenheit)\n')
            try:
                print(calculateData(1,float(Temp)))
                break
            except:
                print("the program expects you to type a number.")
    elif(option == 2):
        while True:
            Miles = input('ok, how fast is the wind going right now? (in miles)\n')
            try:
                print(calculateData(2,float(Miles)))
                break
            except:
                print("the program expects you to type a number.")
    elif(option == 3):
        while True:
            Inches = input('ok, how deep was the snow from the recent snow storm? (in inches) \n')
            try:
                print(calculateData(3,float(Inches)))
                break
            except:
                print("the program expects you to type a number.")
            
#start main code
print("Hello! this program is designed to help convert units of measurement for weather from Fahrenheit to Celsius or imperial to metric!")

#calling fuction
gatherAndShowData()
print("Thank you!")
#End