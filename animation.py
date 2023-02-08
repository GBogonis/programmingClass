#start
import random
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
BLUE = (19,24,98)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screenWidth = 700
screenHight = 500
screenSize = (screenWidth, screenHight)
screen = pygame.display.set_mode(screenSize)
 
pygame.display.set_caption("Animation")

#animation variables
snowList = []

for i in range(100):
    x = random.randrange(0, screenWidth)
    y = random.randrange(0, screenHight)
    snowList.append([x, y])

moonX = 0
moonY = -.1*moonX^2+350
 
# Set variable to run loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event to break loop when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    moonY = (.007*(moonX**2)+(moonX*.25))+100
    # --- Drawing code should go here
    screen.fill(BLUE)
    pygame.draw.rect(screen, (WHITE), pygame.Rect(0, 400, screenWidth, 100))

    #for each snow flake in the list
    for i in range(len(snowList)):
        #drawing the snow
        pygame.draw.circle(screen, WHITE, snowList[i], 2)
        # Move the snow flake down 5 pixel
        snowList[i][1] += 5

        #if the snow flake has moved off the bottom of the screen it gets reset
        if(snowList[i][1] > screenHight):
            #reset it just above the top
            y = random.randrange(-50, -10)
            snowList[i][1] = y
            #give it a new x position
            x = random.randrange(0, screenWidth)
            snowList[i][0] = x
    
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 100 frames per second
    clock.tick(100)
 
# Close the window and quit.
pygame.quit()