#start

#setup
import random
import time
deck = [(1,'ace'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),(10,'ten'),(11,'jack'),(12,'queen'),(13,'king')]
playerScore = 0
botScore = 0

#simple draw random card function
def drawRandom():
    card = random.randrange(0,len(deck))
    return deck[card]

print('Hello and welcome to war! (the card game) are you ready?')

#asks player if they want to start
while True:
    start = input('type "yes" to begin...')
    if(start.lower() == 'yes'):
        print("ok lets begin")
        break
    elif(start.lower() == 'no'):
        print('well too bad, war waits for no one')
        break
    else:
        print('Well when your ready')
time.sleep(1)
#game code

#loop that will draw 2 random cards and compair them to give a point to the person with the higher card
for i in range(10,0,-1):
    #draw cards
    playerCard = drawRandom()
    botCard = drawRandom()
    print('You drew a',playerCard[1], "and your opponent drew a",botCard[1])

    #compairing code
    if(playerCard[0] > botCard[0]):
        print("so you win!")
        playerScore += 1
    elif(botCard[0] > playerCard[0]):
        print("you lost this round")
        botScore += 1
    else:
        print('looks like its a draw')
    time.sleep(.5)

#end screen
if(playerScore > botScore):
    print("You win!")
    print("You scored",playerScore,"points and your opponent only scored",botScore)
elif(botScore > playerScore):
    print("You lose")
    print("You scored",playerScore,"points but your opponent scored",botScore)
else:
    print("Draw!")
    print("You scored",playerScore,"points and your opponent also scored",botScore)

print('Thank you for playing!')
#end