try:
    import pygame
    from pygame.locals import *
    import random
    import math
except:
    print("could not import pygame")
    exit() 

pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)

size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("gaming time")
ballSprite = pygame.image.load("intro_ball.gif")
ballRect = ballSprite.get_rect()

circlePoseX = 360
circlePoseY = 250

moonX = -300


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            print("User asked to quit.")
        '''
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('right')
                circlePoseX += 10
            elif event.key == pygame.K_LEFT:
                print('left')
                circlePoseX -= 10
            elif event.key == pygame.K_UP:
                print('up')
                circlePoseY -= 10
            elif event.key == pygame.K_DOWN:
                print('down')
                circlePoseY += 10
                '''

# --- Game logic should go here
    #moonY = (.007*(moonX**2)+(moonX*.25))+100
# --- Drawing code should go here
    screen.fill(WHITE)

    # draw a green 40 pixel radius circle outline inside rectangle
    #pygame.draw.rect(screen, (BLUE), pygame.Rect(60, 30, 100, 160))
    '''
    pygame.draw.circle(screen,(BLUE),(moonX+500,moonY),10,0)
    moonX += 1
    print('moonY:',moonY)
    print('moonX:',moonX)
    '''

    
    #pygame.draw.polygon(screen,BLACK,((200,100), (10,10), (10,200)),0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)

