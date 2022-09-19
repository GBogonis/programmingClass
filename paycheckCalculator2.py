#start

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

#calculating the pay before and after taxes
if(hoursWorked > 40):
    overtimeHours = hoursWorked-40
else:
    overtimeHours = 0

preTaxPay = round((hoursWorked*payRate)+(overtimeHours*(payRate*1.5)),2)
postTaxPay = round(preTaxPay*0.8,2)

tax = input('and would you like to evade taxes today?\n')

#showing the user the final results 
if(tax == 'yes'):
    print("ok, your total pay is", preTaxPay," you might want to watch out for IRS")
elif(tax == 'no'):
    print("that's ashame, your pay before taxes was", preTaxPay," but after taxes your pay is", postTaxPay)
else:
    print("program expects a yes or no")
    exit()
print("Thank you!")