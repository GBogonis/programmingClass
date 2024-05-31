import random
#start

armors = {"none":0, "leather":5, "bronze":10, "iron":15, "steel":20, "titanium":25}
swords = {"none":0, "wood":-10, "bronze":-20, "iron":-40, "steel":-60, "titanium":-100}
magics = {"fireball": -20, "healing prayer": 30, "great fireball": -50, "great healing preyer": 60}
#(damage, number of turns)
status = {"poison": (-5,5), "fire": (-10,3)}
#enemy values
enemyDamage = {"slime":10, "goblin": 30, "orc": 40}
enemyHealth = {"slime":20, "goblin": 40, "orc": 50}

cavelayer = 10
class player:
    def __init__(self):
        self.health = 100
        self.armor = "none"
        self.sword = "none"
        self.dps = -5
        self.resist = 0

    def turn(self,listOfEnemies):
        while True:
            for i in range(0,len(listOfEnemies),1):
                print("there is a " + listOfEnemies[i].type + "in position " + str(i))
            target = input("Which position do you want to attack?")
            if(int(target) <= len(listOfEnemies)):
                break
        
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
        self.turn = 1

    def turn(self, playerDPS, playerTarget):
        print("you attacked a " + str(enemyList[playerTarget].type) + " for " + str(playerDPS) + " damage!")
        enemyList[playerTarget].health += playerDPS
        for i in enemyList:
            if(i.health > 0):
                mPlayer.health += i.damage
                print("you were hit by a " + str(i.type) + " for " + str(i.damage) + " damage!")
            else:
                enemyList.remove(i)
        print("you are now at " + str(mPlayer.health) + " HP")
        self.turn += 1

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

while cavelayer != 0:
    #encounter:
    difficulty = random.randint(1,10)
    if(difficulty > cavelayer):
        numOfEnemy = 3
    elif(difficulty > cavelayer+2):
        numOfEnemy = 2
    else:
        numOfEnemy = 1
    
    for i in range(numOfEnemy):
        enemyDifficulty = random.randint(1,10)
        if(enemyDifficulty > cavelayer+4):
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

    while(len(enemyList) != 0):
        playerMove = mPlayer.turn()
        mController.turn(playerMove[0], playerMove[1])
    
    cavelayer += 1

print("you have escaped the cave, congratulations!")
    




    