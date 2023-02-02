#start

#gathering info from user
name = input('Hello enployee! What is your name?\n')
print("Ok",name,"this program is designed to help you figure out what you paycheck should be!")
hourlyRate = input('so, how much money do you make per hour?\n')
hoursWorked = input('and how many hours did you work\n')
print("ok",name,"you worked",float(hoursWorked),"for",round(float(hourlyRate),2),"$ per hour")
correct = input('correct? (yes or no)\n')

#asking if the users info is correct
if(correct == "yes"):
    print("ok great!")
    #asking the user if they want to evade taxes is always a good thing to do
    tax = input('so would you like to evade taxes today? (yea or no)\n')
    cont = True
elif(correct == "no"):
    print("I recomend restarting then")
    tax = 'no'
    cont = False


if(tax == "yes" and cont):
    print("correct choice, your total gross income is",float(hourlyRate)*float(hoursWorked),"$")
    print("we recomend that you watch out for the IRS")
elif(tax == "no" and cont):
    #calculating taxes 
    print("thats ashame you could have gotten", float(hourlyRate)*float(hoursWorked),"$")
    print("your pay after taxes", round((float(hourlyRate)*float(hoursWorked))*0.8,2),"$")

print("Thank you!")