import random
#start
armors = {"none":0, "leather":5, "bronze":10, "iron":15, "titanium":20}
swords = {"none":0, "wood":-10, "bronze":-20, "iron":-40, "titanium":-60}
#enemy values
enemyDamage = {"slime": -15, "goblin": -25, "orc": -35}
enemyHealth = {"slime":20, "goblin": 40, "orc": 50}

#keeps track of game progress, and affects difficulty
cavelayer = 10

#player class to manage player state and calculate the players actions
class player:
    def __init__(self):
        #base stats
        self.health = 100
        self.armor = "none"
        self.sword = "none"
        self.dps = -5

    def turn(self,listOfEnemies):
        #turn code is inside a loop to ensure the user input is viable
        while True:
            try:
                #simple code for "you are being attacked, what do you do?"
                for i in range(0,len(listOfEnemies),1):
                    print("there is a " + listOfEnemies[i].type + " in position " + str(i+1))
                target = input("Which position do you want to attack?")
                target = int(target)
                if(target <= len(listOfEnemies)):
                    break
            except:
                print("intput not recognized, try again")
        #returns values that the controller class takes as a argument to calculate what happens in a turn
        self.dps = -5 + swords[self.sword]
        return (self.dps, target)

class enemy:
    def __init__(self, type):
        self.health = enemyHealth[type]
        self.damage = enemyDamage[type]
        self.type = type
        

#handles turns and interactions
class controller:
    def __init__(self):
        self.turns = 1

    def turn(self, playerDPS, playerTarget, playerResist):
        #takes the players actions and makes the game happen
        if(mPlayer.health > 0):
            #logic to make wording better
            if((enemyList[playerTarget-1].health + playerDPS) > 0):
                print("you attacked a " + str(enemyList[playerTarget-1].type) + " for " + str(-playerDPS) + " damage, it has ", (enemyList[playerTarget-1].health + playerDPS), " HP left!")
            else:
                print("you attacked a " + str(enemyList[playerTarget-1].type) + " for " + str(-playerDPS) + " damage")
            #where the enemies take damage
            enemyList[playerTarget-1].health += playerDPS
            if(enemyList[playerTarget-1].health <= 0):
                print("you have slain the ", enemyList[playerTarget-1].type)
            #where you take damage
            for i in enemyList:
                if(i.health > 0):
                    mPlayer.health += (i.damage + playerResist)
                    print("you were hit by a " + str(i.type) + " for " + str(-(i.damage)) + " damage!" + " you are now at " + str(mPlayer.health) + " HP")
                else:
                    enemyList.remove(i)
        #turns varible that we display at the end
        self.turns += 1

#game instance setup
enemyList = []
mPlayer = player()
mController = controller()

#game loop
while True:
    start = input("start game? [Y or N]")
    if(start == "N" or start == "n"):
        exit()
    elif(start == "Y" or "y"):
        print("You wake up in a cave, and you decide the only reasonable course of action is to indulge your sense of adventrue and escape this cave! \n")
        break
    else:
        print("input not recognized: try again \n")

#where the magic happens
while cavelayer != 0:
    #encounter setup:
    difficulty = random.randint(1,10)
    if(difficulty > cavelayer):
        numOfEnemy = 3
    elif(difficulty > cavelayer+2):
        numOfEnemy = 2
    else:
        numOfEnemy = 1
    
    for i in range(numOfEnemy):
        enemyDifficulty = random.randint(1,10)
        if(enemyDifficulty > cavelayer+5):
            enemyList.append(enemy("orc"))
        elif(enemyDifficulty > cavelayer):
            enemyList.append(enemy("goblin"))
        else:
            enemyList.append(enemy("slime"))
    if(numOfEnemy == 3):
        print("you are on floor: " + str(cavelayer) + " and you are confronted by three enemies, a " + enemyList[0].type + ", a " + enemyList[1].type + ", and a " + enemyList[2].type)
    elif(numOfEnemy == 2):   
        print("you are on floor: " + str(cavelayer) + " and you are confronted by two enemies, a " + enemyList[0].type + ", and a " + enemyList[1].type)
    else:
        print("you are on floor: " + str(cavelayer) + " and you are confronted by a enemy, a " + enemyList[0].type)

    #encounter gameplay:
    while(len(enemyList) != 0):
        #while there are enemies to fight, fight!
        playerMove = mPlayer.turn(enemyList)
        mController.turn(playerMove[0],playerMove[1], armors[mPlayer.armor])
        #we need two breaks for both loops in the event of a game over.
        if(mPlayer.health <=0):
            break
    if(mPlayer.health <=0):
        break
    #the battle is over, take a rest

    #funny messages
    floorMessage = random.randint(1,5)
    if(floorMessage == 1):
        print("floor complete! you might make it out of this alive")
    elif(floorMessage == 2):
        print("floor complete! you start to feel like a true hero")
    elif(floorMessage == 3):
        print("floor complete! if you knew magic this would be a lot easier")
    elif(floorMessage == 4):
        print("floor complete! you are suprised at your own capability")
    elif(floorMessage == 5):
        print("floor complete! if you make it out of here, you wonder who you will tell about this")

    #loot time, drop rarity is calculated by cave layer, similar to enemy difficulty
    #this if is to make the ending of the game smoother, we don't need loot if we beat the game
    if(cavelayer != 1):
        print("you rest for a bit and scavange the battlefield")
        #health reset
        mPlayer.health = 100

        #sword drops 
        lootSword = random.randint(1,10)
        if(lootSword > cavelayer+5 and mPlayer.sword != "titanium"):
            print("You find a titanium sword! it's heavy but you can deal")
            mPlayer.sword = "titanium"
        elif(lootSword > cavelayer+2 and mPlayer.dps > -40):
            print("You find a iron sword! it's lighter than you expect but the handle has seen better days")
            mPlayer.sword = "iron"
        elif(lootSword > cavelayer and mPlayer.dps > -20):
            print("You find a bronze sword! part of the blade is chiped but it cuts fine")
            mPlayer.sword = "bronze"
        elif(mPlayer.dps > -10):
            print("You find a wood sword! it isn't great but it better than nothing")
            mPlayer.sword = "wood"
        else:
            print("You couldn't find a better weapon")

        #armor drops
        lootArmor = random.randint(1,10)
        if(lootArmor > cavelayer+5 and mPlayer.armor != "titanium"):
            print("You find titanium armor! you might as well be a real knight at this point")
            mPlayer.armor = "titanium"
        elif(lootArmor > cavelayer+2 and armors[mPlayer.armor] < 15):
            print("You find iron armor! you pretend you are a knight to feel better about the situation")
            mPlayer.armor = "iron"
        elif(lootArmor > cavelayer and armors[mPlayer.armor] < 10):
            print("You find bronze armor! you wonder if the Ancient Greeks were the last ones here")
            mPlayer.armor = "bronze"
        elif(mPlayer.dps > -10):
            print("You find leather armor! you don't know what animal's leather but that doesn't matter now")
            mPlayer.armor = "leather"
        else:
            print("You couldn't find any better protection")
    #we're moving up in the world
    cavelayer -= 1

#if we got to this part, you either beat the game or died trying 
if(mPlayer.health <=0):
    print("not everyone makes it out alive...")
    print("GAME OVER, You survived " , str(mController.turns), " turns.")
else:
    print("you have escaped the cave, congratulations!")
    print("GAME WIN, You made it out in ", str(mController.turns), " turns.")

print("thank you for playing")