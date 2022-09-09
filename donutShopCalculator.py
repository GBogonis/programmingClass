#var set-up
costOfDozen = 4.99
costOfSingle = costOfDozen/12
costOfCoffee = 2.99

#calculating how many donuts and coffees the user wants and how much it will cost

prompt = 'How many donuts would you like?\n'
donutsWanted = input(prompt)

if(int(donutsWanted) > 12):
    print("only 12 in stock, sorry")
else:
    cost = cost + round(int(donutsWanted)*costOfSingle,2)
    #print("that will cost", cost, "$")

prompt2 = 'and would you like any coffee?\n'
coffeeWanted = input(prompt2)

cost = cost + round(int(coffeeWanted)*costOfCoffee,2)
print("Ok, Your total cost is", round(cost,2),"$")

#calculating how much money is owed compaired to how much money is given

prompt3 = 'How much can you pay?\n'
amountPaid = input(prompt3)

if(int(amountPaid) < cost):
    print("You are short", round(abs(int(amountPaid)-cost),2), "$")
elif(int(amountPaid) > cost):
    print("You over paid", round(int(amountPaid)-cost,2),"$")
else:
    print("You paid the exact amount needed!")

print("Thank You")