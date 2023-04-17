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
screenHight = 700
screenWidth = 1000
size = (screenWidth, screenHight)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Pygame")

#useful rect docs
#https://pygame.readthedocs.io/en/latest/rect/rect.html
# load ball image
ballSprite = pygame.image.load("intro_ball.gif")
ballRectList = []
ballSpeedList = []
for i in range(4):
    ballSpeedList.append([5,5])
    ballRect = ballSprite.get_rect()
    ballRect.x = random.randrange(0, screenWidth-111)
    ballRect.y = random.randrange(0, screenHight-111)
    ballRectList.append(ballRect)
'''
class ball():
    def __init__(self,pos):
        self.pos = pos
'''      


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
 
    screen.fill(colors["BLACK"]) # note we refill the screen w/ black every flip() so no ghost trails :)
    # --- Game logic should go here
    for i in range(len(ballRectList)):
        ballRectList[i] = ballRectList[i].move(ballSpeedList[i])
        
        if ballRectList[i].left < 0 or ballRectList[i].right > screenWidth: # uses edges of ballRectList[i] surface to detect collision with screen surface
            ballSpeedList[i][0] = -ballSpeedList[i][0] # reverse horizontal speed to stay on screen
        if ballRectList[i].top < 0 or ballRectList[i].bottom > screenHight:
            ballSpeedList[i][1] = -ballSpeedList[i][1] # reverse vertical speed to stay on screen

        for e in range(len(ballRectList)):
            if(e != i):
                
                if ballRectList[i].colliderect(ballleftE):
                    ballSpeedList[e][0] = -ballSpeedList[e][0]
                    print("I collide E: left")
                if ballRectList[i].colliderect(balltopE):
                    ballSpeedList[e][1] = -ballSpeedList[e][1]
                    print("I collide E: top")
                if ballRectList[i].colliderect(ballrightE):
                    ballSpeedList[e][0] = -ballSpeedList[e][0]
                    print("I collide E: right")
                if ballRectList[i].colliderect(ballbottomE):
                    ballSpeedList[e][1] = -ballSpeedList[e][1]
                    print("I collide E: bottom")
                
                if ballRectList[e].colliderect(ballleft):
                    ballSpeedList[i][0] = -ballSpeedList[i][0]
                    print("E collide I: left")
                if ballRectList[e].colliderect(balltop):
                    ballSpeedList[i][1] = -ballSpeedList[i][1]
                    print("E collide I: top")
                if ballRectList[e].colliderect(ballright):
                    ballSpeedList[i][0] = -ballSpeedList[i][0]
                    print("E collide I: right")
                if ballRectList[e].colliderect(ballbottom):
                    ballSpeedList[i][1] = -ballSpeedList[i][1]
                    print("E collide I: bottom")
        screen.blit(ballSprite, ballRectList[i])
 
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)
 
# Close the window and quit.
pygame.quit()
