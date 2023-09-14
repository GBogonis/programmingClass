#start
try:
    import pygame
    from pygame.locals import *
    import random
except:
    print("could not import pygame")
    exit() 
    
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
#I made a dictionary for colors, similar it a "enum" in java
colors = {'BLACK':(0,0,0),"WHITE":(255, 255, 255),"GREEN":(0, 255, 0),"RED":(255, 0, 0),"BLUE":(0, 0, 255)}
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screenHight = 665
screenWidth = 1000
size = (screenWidth, screenHight)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Pygame")

pygame.mixer.init() 
#snowy forest background image and a cartoon moose image
forestBackground = pygame.image.load("snow_forest.jpg")
moose = pygame.image.load("moose_image.png")

#sound file
mooseSound = pygame.mixer.Sound("mooseSound.ogg")
 
#snow animation stuff
#animation variables
snowList = []

for i in range(100):
    x = random.randrange(0, screenWidth)
    y = random.randrange(0, screenHight)
    snowList.append([x, y])
# Set variable to run loop until the user clicks the close button.
going = True
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while going:
    # --- Main event to break loop when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if the player clicks, it plays a moose sound
            mooseSound.play()
 
    # --- Game logic should go here
    
 
    # --- Drawing code should go here
    #setting the background image of the snowy forest
    screen.blit(forestBackground,(0,0))
    
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
    
    #adding the moose image where the mouse is but off-set to center the image
    screen.blit(moose,(pygame.mouse.get_pos()[0]-110,pygame.mouse.get_pos()[1]-110))
    
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    #making the mouse invisible so it doesn't overlap the image
    pygame.mouse.set_visible(False)
 
# Close the window and quit.
pygame.quit()
