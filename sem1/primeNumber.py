#start
#list of numbers
numlist = [611,612,613,617,73,77,79,5403,5402,5407,669,1188,1189]

def primeNumCheck(num):
    #just making sure it isn't 1
    if num == 1:
        return False
    elif num > 1:
        #checking for any possible factors
        for i in range(2, num):
            if((num % i) == 0):
                #if a factor is found then it will return true
                return True
    else:
        #if no factors are found
        return False

#putting every number through the function and printing the results
for num in numlist:
    if(primeNumCheck(num)):
        print(num, "is a prime number")
    else:
        print(num, 'is not a prime number')
#end