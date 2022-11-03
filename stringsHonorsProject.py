#start

#function to easily convert the fraction to a decimal
def fractionToDecimal(a,b):
    return a/b


#intro
print("Hello! this program will convert a fraction to a decimal.")


#4 different checks to make sure there aren't any errors
while True:
    #taking input
    fractionStr = input('please inter the fraction you want to convert (xx/yy format please)\n')

    #checks for a "/"
    if(fractionStr.find('/')>=0):
        #using the position of the "/" in the string to divide it up and to get our numbers
        slashPos = fractionStr.find('/')
        numerator = fractionStr[:slashPos]
        denominator = fractionStr[slashPos+1:]
        try:
            numerator = int(numerator)
            denominator = int(denominator)
            if(denominator == 0):
                print("can't devide by 0")
            else:
                break
        except:
            print('make sure you have 2 whole numbers divided by a "/"')
    else:
        print('make sure your fraction has a "/" in it')

#printing out final results 
print("you decimal is", fractionToDecimal(numerator,denominator))
print("Thank you!")