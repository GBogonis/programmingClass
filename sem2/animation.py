#start
import random
import math
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
BROWN = (150, 75, 0)
GREY = (100,100,100)
MOON_GREY = (48, 70, 96)
 
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

    # --- Drawing code should go here
    screen.fill(BLUE)
    #ground
    pygame.draw.rect(screen, (WHITE), pygame.Rect(0, 400, screenWidth, 100))

    #moon
    pygame.draw.circle(screen, (MOON_GREY), (15,15), 60)
    pygame.draw.circle(screen, (GREY), (20,40), 15)
    pygame.draw.circle(screen, (GREY), (50,10), 10)

    #snow flake stuff
    #for each snow flake in the list
    for i in range(len(snowList)):
        #drawing the snow
        pygame.draw.circle(screen, WHITE, snowList[i], 2)
        #move the snow flake down 5 pixel so it looks like it's falling
        snowList[i][1] += 5

        #if the snow flake has moved off the bottom of the screen it gets reset
        if(snowList[i][1] > screenHight):
            #reset it just above the top
            y = random.randrange(-50, -10)
            snowList[i][1] = y
            #give it a new x position
            x = random.randrange(0, screenWidth)
            snowList[i][0] = x
    
    #snowman stuff
    
    #stick arms
    pygame.draw.line(screen, (BROWN), (300,240), (250,150) ,4)
    pygame.draw.line(screen, (BROWN), (400,240), (450,350) ,4)
    #snowman body
    pygame.draw.circle(screen, (WHITE), (350,340), 75)#bottom
    pygame.draw.circle(screen, (WHITE), (350,240), 55)#middle
    pygame.draw.circle(screen, (WHITE), (350,160), 35)#top
    #top hat
    pygame.draw.rect(screen,(BLACK), pygame.Rect(325,120,50,10))
    pygame.draw.rect(screen,(BLACK), pygame.Rect(335,90,30,40))
    #face
    pygame.draw.circle(screen, (BLACK), (340,150), 7)
    pygame.draw.circle(screen, (BLACK), (360,150), 7)
    pygame.draw.arc(screen, (BLACK), [330,145,40,40], math.pi/1, math.pi/18, 3)

    

    
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 100 frames per second
    clock.tick(100)
 
# Close the window and quit.
pygame.quit()