#start
try:
    import pygame
    from pygame.locals import *
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
screenHight = 665
screenWidth = 1000
size = (screenWidth, screenHight)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Pygame")

#image stuff
forestBackground = pygame.image.load("snow_forest.jpg")
moose = pygame.image.load("moose_image.png")
 
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
 
    # --- Game logic should go here
    
 
    # --- Drawing code should go here

    screen.blit(forestBackground,(0,0))
    screen.blit(moose,(pygame.mouse.get_pos()[0]-110,pygame.mouse.get_pos()[1]-110))
    
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    pygame.mouse.set_visible(False)
 
# Close the window and quit.
pygame.quit()
