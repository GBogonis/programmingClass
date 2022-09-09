#start

#gathering info from user
name = input('Hello enployee! What is your name?\n')
print("Ok",name,"this program is designed to help you figure out what you paycheck should be!")
hourlyRate = round(input('so, how much money do you make per hour?\n'),2)
hoursWorked = input('and how many hours did you work\n')
print("ok",name,"you worked",hoursWorked,"for",hourlyRate,"per hour")
correct = input('correct? (yes or no)\n')

#asking if the users info is correct
if(correct == "yes"):
    print("ok great!")
    #asking the user if they want to evade taxes is always a good thing to do
    tax = input('so would you like to evade taxes today?\n')
    cont = True
elif(correct == "no"):
    print("I recomend restarting then")
    cont = False


if(tax == "yes",cont):
    print("correct choice, your total gross income is",hourlyRate*hoursWorked)
    print("we recomend that you watch out for the IRS")
elif(tax == "no",cont):
    print("thats ashame")