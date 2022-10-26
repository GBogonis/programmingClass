#start

#making the list and a var for the total of the even numbers
numlist = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4, 13]
sumOfEven = 0

#for x in numlist will run once per each item in the list
for x in numlist:
    #this if logic will check if a number is even or odd be deviding it by 2 and if the remainder is anything other than 0 it is odd
    if (int(x) % 2)==0:
        sumOfEven += x
        print(x, "is even")
    else:
        print(x, "is odd")
print(sumOfEven, "is the sum of all the even numbers!")