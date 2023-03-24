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
colors = {'BLACK':(0,0,0),"WHITE":(255, 255, 255),"GREEN":(0, 255, 0),"RED":(255, 0, 0),"BLUE":(0, 0, 255)}
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screenHight = 500
screenWidth = 700
size = (screenWidth, screenHight)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Pygame")
 
# load ball image 
ballSprite = pygame.image.load("intro_ball.gif")
# frame surface of the rectanglular dimensions of the ball surface



#animation variables
snowList = []
snowListSpeed = []

for i in range(5):
    x = random.randrange(0, screenWidth)
    y = random.randrange(0, screenHight)
    speed = [5, 5]
    snowList.append([x, y])
    snowListSpeed.append(speed)
 
#animation variables
ballList = []
ballListSpeed = []
ballPos = []
ballSpeed = [5, 5]

for i in range(5):
    ballPos.append([random.randrange(0, screenWidth),random.randrange(0, screenHight)])
    ballListSpeed.append(ballSpeed)
    ballrect = ballSprite.get_rect()
    ballList.append(ballrect)
    
    

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
   
    screen.fill(colors["BLACK"]) # note we refill the screen w/ black every flip() so no ghost trails :)

    '''
    # --- Drawing code should go here
    for i in range(len(snowList)):
        #drawing the snow
        pygame.draw.circle(screen, colors["BLUE"], snowList[i], 10)
        #screen.blit(ball, snowList[i])
        
        #move the snow flake down 5 pixel so it looks like it's falling
        snowList[i][0] += snowListSpeed[i][0]
        snowList[i][1] += snowListSpeed[i][1]

        if snowList[i][0] < 11 or snowList[i][0] > screenWidth-11: # uses edges of ballrect surface to detect collision with screen surface
            snowListSpeed[i][0] = -snowListSpeed[i][0] # reverse horizontal speed to stay on screen
        if snowList[i][1] < 11 or snowList[i][1] > screenHight-11:
            snowListSpeed[i][1] = -snowListSpeed[i][1] # reverse vertical speed to stay on screen
    '''

    for i in range(len(ballList)):
        ballPos[i][0] += ballListSpeed[i][0]
        ballPos[i][1] += ballListSpeed[i][1]
        screen.blit(ballSprite,ballPos[i])
        if ballPos[i][0] < 11 or ballPos[i][0] > screenWidth-11: # uses edges of ballrect surface to detect collision with screen surface
            ballListSpeed[i][0] = -ballListSpeed[i][0] # reverse horizontal speed to stay on screen
        if ballPos[i][1] < 11 or ballPos[i][1] > screenHight-11:
            ballListSpeed[i][1] = -ballListSpeed[i][1] # reverse vertical speed to stay on screen

        

    #screen.blit(ball, ballrect) # screen.blit takes 2 params - the first, ball, is drawn onto the second, ballrect surface
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
