#test
#from ctypes.wintypes import PINT
import time
import random
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
'''
fhand = open('scrabble_wds.txt')
linee = fhand.read()

word = input('word?\n')
word = word.lower()
print(word)
if word in linee:
    print('pog')
