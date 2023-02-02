#var setup
costOfDozen = 4.99
costOfSingel = costOfDozen/12
costOfCoffee = 2.99
cont = False
cont2 = False

#start

#asking user if they want to accept the first offer
print("your friend wants to buy a donut from you for 1$")
cont = input('do you accept? yes or no\n')
if(cont == "yes"):
    print("you owe your friend", round(abs(costOfSingel-1),2))
elif(cont == "no"):
    print("ok then :(")

#asking user if they want to continue to the next part
if (input('do you want to continue? yes or no\n') == "yes"):
    print("ok, your friend wants 2 donuts now and wants you to buy them a coffee and they give you 20$")
    cont2 = True
elif(input('do you want to continue? yes or no\n') == "no"):
    print("oh.. ok then :(")
    cont2 = False

#result of second offer
if(cont2 == True):
    print("you owe your friend", round(abs(20-((costOfDozen*2)+costOfCoffee)),2), "$")
elif(cont2 == False):
    print("your friend doesn't like you now")
print("end")