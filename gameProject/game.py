try:
    import pygame
    import random
    import enemy
except:
    print("could not import pygame")
    exit() 
    
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colors = {'BLACK':(0,0,0),"WHITE":(255, 255, 255),"GREEN":(0, 255, 0),"RED":(255, 0, 0),"BLUE":(0, 0, 255)}
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screenWidth = 700
screenHight = 700
screenSize = (screenWidth, screenHight)
screen = pygame.display.set_mode(screenSize)
 
pygame.display.set_caption("My Pygame")

 
# Set variable to run loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()

playerPosX = 350
playerPosY = 250
playerPos = playerPosX, playerPosY
playerHealth = 250


attacking = False
'''
#animation variables
enemyList = []


for i in range(10):
    x = random.randrange(0, screenWidth)
    y = random.randrange(0, screenHight)
    enemyList.append([x, y])

def drawEnemy(pos):
    pygame.draw.circle(screen, BLACK, pos, 2)
'''
# -------- Main Program Loop -----------
while not done:
    # --- Main event to break loop when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            attacking = True
        

    # --- Game logic should go here
    

    

    # --- Drawing code should go here
    screen.fill(colors["WHITE"])
    pygame.draw.circle(screen,(BLUE),(playerPos),50)
    if(attacking):
        target = pygame.mouse.get_pos()
        currentPos =[playerPos]
        pygame.draw.circle(screen,(colors["RED"]),(pygame.mouse.get_pos()),10)
        attacking = False

    '''
    for i in range(len(enemyList)):
        #drawing the snow
        pygame.draw.circle(screen, BLACK, enemyList[i], 2)
        drawEnemy(enemyList[i])
        #move the snow flake down 5 pixel so it looks like it's falling

        if(enemyList[i][0] < playerPosX):
            enemyList[i][0]  += playerPosX/1000
        elif(enemyList[i][0] > playerPosX):
            enemyList[i][0]  -= playerPosX/1000
        if(enemyList[i][1]  < playerPosY):
            enemyList[i][1]  += playerPosY/1000
        elif(enemyList[i][1]  > playerPosY):
            enemyList[i][1]  -= playerPosY/1000
    '''

    
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
