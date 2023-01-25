#test
#from ctypes.wintypes import PINT
import time
import random
import csv
import pygame

'''
numm = input('pick a number\n')
numm = int(numm)


#proper setup for a try&except in a loop
while True: 
    num = input('pick a number \n')
    try:
        if(float(num) == 1):
            print('cool')
            break
    except:
        print('i said a number dummy :3')


#0 in the minimum and 55 is max, it will add the -5 to i every loop and will only run the code when i is in that range
for numm in range(0,int(numm)+1,5):
    print(numm)
'''

#while True:
    #print(random.randint(1,20))
'''
num = input("Enter any number to test whether it is odd or even:\n")


if (int(num) % 2)==0:
    print("The number is even")
else:
    print("The provided number is odd")

numlist = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4, 13]

for x in numlist:
    print(x)


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

print("Fake Python".replace("Fake", "Real"))

print("Yes or no?")
answer = input(' > ')
if(answer.lower() == 'yes'):
    print('pog')
else:
    print('cringe')
    
word_file = open("scrabble_wds.txt")
word = 'abandoning'
for line in word_file:
    if(line.find(word) != -1):
        print('pog')  
        break 
    else:
        print('cringe')
print('end')


for line in fhand:
    line = line.rstrip()
    if line.find('aah') == -1: continue
    print(line)

fhand = open('scrabble_wds.txt')
linee = fhand.read()

word = input('word?\n')
word = word.lower()
print(word)
if word in linee:
    print('pog')



# open the file in read mode
filename = open('peoples.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
people = []


# iterating over each row and append
# values to empty list
for col in file:
	people.append(col['Goat'])

# printing lists
#print('People:', people)


try:
    fhand = open('Abe_Lincoln_speech.txt')
except:
    print('File cannot be opened:')
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

fin_max = max(counts, key=counts.get)
thing = counts.get(fin_max)
print(thing)
print("Maximum value:",fin_max)


word = input('>')
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
palindrome = word + reverse(word)
print(palindrome)

# Program to check if a number is prime or not

example = 29

# To take input from the user
#num = int(input("Enter a number: "))

numlist = [611,612,613,617,73,77,79,5403,5402,5407,669,1188,1189]

def primeNumCheck(num):
    flag = False
    if num == 1:
        flag = False
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        return flag

for num in numlist:
    if(primeNumCheck(num)):
        print(num, "is a prime number")
    else:
        print(num, 'is not a prime number')
        '''


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