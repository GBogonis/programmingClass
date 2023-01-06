# solve these python bugs and/or incorrect results
# add a comment to problem each explaining what you found
# and how to fix it

# number 1 - add some numbers

inta = 10
#the '2O' was typed with a letter 'O' instead of the number 0
intb = 20
intc = 30

print(inta + intb + intc)

# number 2 - count items in a list

mylist = (2, 4, 6, 8, 22, 44, 66, 88)
#forgot to define 'summy' before the loop and they typed 'num' instead of 'nummy' in the loop
summy = 0
for nummy in mylist:
    summy += nummy

print(summy)

# number 3 - add some numbers

int = 12
intb = 14
#13 was defined as a string not a int
intc = 13
#2 numbers cannot be multiplied by putting one in '()' instead use a '*'
intd = int*intb
inte = int + intb + intd
print(inte)


# number 4 - say hi to all the people in a list

namelist = ("Fred", "Sally", "Pete", "Emma", "Linus")
#you can use the namelist, no need for a range loop
for i in namelist:
    #replace the var that changes with the name instead of a number the corisponds to a name on the list 
    print("Hi", i)

# number 5 - age sort

print("I am sorting people by age. Enter your age.")
#added a try around the age input to ensure a usable number
while True:
    age = input(" > ")
    try:
        print(type(age))
        age = int(age)
        
        print(type(age))
        break
    except:
        print('age needs to be a whole number')

#the numbers being compaired were in quoat marks so they were strings not INTs
if age < 13:
    print("kid")
elif age < 20:
    print("teen")
else:
    print("adult")

# number 6 - sum a list of numbers

listy = (3,4,5,6,7,8)
sum = 0
sum = sum(listy)
print(sum)

# number 7 - sum a list of numbers

listy = (9,8,7,6,5,4,3,2,1)
for num in listy:
    summy = 0
    summy += num
print("The sum is", summy)

# number 8 - functions

def funcA():
    myname = "JR"
    myage = 70

def funcB():
    if myage > 65:
        print("You can retire")

funcA()
funcB()

# number 9 functioons - output?

def area():
    x = 3
    y = 4
    rectarea = x * y
    return rectarea

area()

# 10 countdown backwards in a list

listy = (1,2,3,4,5,6,7,8,9,10)
for i in range(len(listy), 0, -1):
    print(listy[i])
