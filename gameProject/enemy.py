try:
    import pygame.locals
    import random
    import game
except:
    print("could not import")
    exit()


#animation variables
enemyList = []

for i in range(10):
    x = random.randrange(0, game.screenSize)
    y = random.randrange(0, game.screenHight)
    enemyList.append([x, y])

def drawEnemy(pos):
    
    for i in range(len(enemyList)):
            #drawing the snow
            pygame.draw.circle(game.screen, game.colors['BLACK'], enemyList[i], 2)
            pygame.draw.circle(game.screen, game.colors["BLACK"], enemyList[i], 2)
            #move the snow flake down 5 pixel so it looks like it's falling

            if(enemyList[i][0] < playerPosX):
                enemyList[i][0]  += playerPosX/1000
            elif(enemyList[i][0] > playerPosX):
                enemyList[i][0]  -= playerPosX/1000
            if(enemyList[i][1]  < playerPosY):
                enemyList[i][1]  += playerPosY/1000
            elif(enemyList[i][1]  > playerPosY):
                enemyList[i][1]  -= playerPosY/1000