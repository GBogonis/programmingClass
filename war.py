#start

#setup
import random
import time
deck = [(1,'ace'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),(10,'ten'),(11,'jack'),(12,'queen'),(13,'king')]
playerScore = 0
botScore = 0

#simple draw random card function
def drawRandom():
    return random.randrange(0,len(deck))

print('Hello and welcome to war! (the card game) are you ready?')

while True:
    start = input('type "yes" to begin...')
    if(start == 'yes'.lower()):
        print("ok lets begin")
        break
    elif(start == 'no'.lower()):
        print('well too bad, war waits for no one')
        break
    else:
        print('Well when your ready')

for i in range(10,0,-1):
    


    
