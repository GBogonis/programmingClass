#start

#function to easily convert the fraction to a decimal
def fractionToDecimal(a,b):
    return a/b


#intro
print("Hello! this program will convert a fraction to a decimal.")

#I used 2 "while true" loops, one for making sure the user gave a whole number and the other to make sure the user gave a positive number 
while True:
    while True:
        #logic for ensuring a whole number
        fractionA = input('what is the numerator of the fraction?\n')
        try:
            fractionA = int(fractionA)
            break
        except:
            print('The program wants a positive whole number')
    #logic to ensure a positive number
    if(fractionA>0):
        break
    else:
        print('The program can only work with positive numbers')

while True:
    while True:
        #logic for ensuring a whole number
        fractionB = input('and what is the denominator of the fraction?\n')
        try:
            fractionB = int(fractionB)
            break
        except:
            print('The program wants a positive whole number')
    #logic to ensure a positive number
    if(fractionB>0):
        break
    else:
        print('The program can only work with positive numbers')

#printing out final results 
print("you decimal is ", fractionToDecimal(fractionA,fractionB))
print("Thank you!")