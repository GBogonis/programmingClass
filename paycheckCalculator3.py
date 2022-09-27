#start

#function setup
def calculatePay(hours, rate):
    if (hours > 40):
        return (hours*rate) + ((hours-40)*(rate*1.5))
    else:
        return hours*rate

def calculateTaxes(pay, taxRate):
    #its expected that the tax% will be in a decimal form
    return pay*taxRate

#collecting info from user
print("Hello employee, this program will help you calculate your pay!")

#setup in a way to avoid errors and end code in a nice way
try:
    payRate = float(input('First what is your hourly pay?\n'))
except:
    print("program expects a number")
    exit()

try:
    hoursWorked = int(input('and how many hours did you work?\n'))
except:
    print("program expects a whole number")
    exit()



tax = input('and would you like to evade taxes today?\n')

#showing the user the final results 
if(tax == 'yes'):
    print("ok, your total pay is $", round(calculatePay(hoursWorked, payRate),2)," you might want to watch out for IRS")
elif(tax == 'no'):
    print("that's ashame, your pay before taxes was $", round(calculatePay(hoursWorked, payRate),2)," but after taxes your pay is $", round(calculateTaxes(calculatePay(hoursWorked, payRate), .8),2))
else:
    print("program expects a yes or no")
    exit()
print("Thank you!")