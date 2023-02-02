try:
    import pygame
except:
    print("could not import pygame")
    exit() 
    
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Pygame")
 
# Set variable to run loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()

playerPosX = 350
playerPosY = 250
playerPos = playerPosX, playerPosY
playerHealth = 250

enemyPosX = 0
enemyPosY = 0
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event to break loop when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here
    if(enemyPosX != playerPosX):
        enemyPosX += playerPosX/100
    if(enemyPosY != playerPosY):
        enemyPosY += playerPosY/100

    

    # --- Drawing code should go here
    screen.fill(WHITE)
    pygame.draw.circle(screen,(BLUE),(playerPos),50)
    pygame.draw.circle(screen,(RED),(enemyPosX,enemyPosY),30)
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
