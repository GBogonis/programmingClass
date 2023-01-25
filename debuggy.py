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

#renamed 'int' to 'inta' because having a var named int messes stuff up 
inta = 12
intb = 14
#13 was defined as a string not a int
intc = 13
#2 numbers cannot be multiplied by putting one in '()' instead use a '*'
intd = inta*intb
inte = inta + intb + intd
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
    try:
        age = input(" > ")
        age = int(age)
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
#changed listy to a list by added square brackets 
listy = [3,4,5,6,7,8]
#changed the name of the var to something that wasen't being used
summyy = 0
summyy = sum(listy)
print(summyy)

# number 7 - sum a list of numbers
#changed the name of the list to something that was unused
listyy = (9,8,7,6,5,4,3,2,1)
#declaring the var outside of the loop so it doen't reset every time, and used different name
summy1 = 0
for num in listyy:
    summy1 += num
print("The sum is", summy1)

# number 8 - functions
#made the vars in the function global so both function could use it
def funcA():
    global myname
    myname = "JR"
    global myage
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
#calling the function by itself wont do anything, but calling it in a print will output the result
print('area is', area())


# 10 countdown backwards in a list

listy1 = (1,2,3,4,5,6,7,8,9,10)
#got rid of the range part of the loop, instead it just interates through the list in reverse
for i in reversed(listy1):
    #just prints the item from the loop not directly through the list
    print(i)
