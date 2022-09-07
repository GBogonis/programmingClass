#var set-up
costOfDozen = 4.99
costOfSingle = costOfDozen/12

#calculating how many donuts the user wants and how much it will cost

prompt = 'How many donuts do you want?\n'
donutsWanted = input(prompt)

if(int(donutsWanted) > 12):
    print("only 12 in stock, sorry")
else:
    cost = round(int(donutsWanted)*costOfSingle,2)
    print("that will cost", cost, "$")

#calculating how much money is owed compaired to how much money is given

prompt2 = 'How much can you pay?'
amountPaid = input(prompt2)

if(int(amountPaid) < cost):
    print("You are short", abs(int(amountPaid)-cost), "$")
elif(int(amountPaid) > cost):
    print("You over paid", int(amountPaid)-cost,"$")
else:
    print("You the exact amount needed!")
