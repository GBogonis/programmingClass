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


# load ball image
ballSprite = pygame.image.load("intro_ball.gif")
ballRectList = []
ballSpeedList = []
for i in range(3):
    ballSpeedList.append([5,5])
    ballRect = ballSprite.get_rect()
    ballRect.x = random.randrange(0, screenWidth-111)
    ballRect.y = random.randrange(0, screenHight-111)
    ballRectList.append(ballRect)




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
        #moving the ball based on current speed values
        ballRectList[i] = ballRectList[i].move(ballSpeedList[i])
        
        #screen boarder collision
        if(ballRectList[i].left < 0 or ballRectList[i].right > screenWidth):
            ballSpeedList[i][0] = -ballSpeedList[i][0] #reverse horizontal speed so the ball stays on the screen
        if(ballRectList[i].top < 0 or ballRectList[i].bottom > screenHight):
            ballSpeedList[i][1] = -ballSpeedList[i][1] #same with the vertical speed

        #creating vars for the sides of the ball for collision logic
        balltop = (ballRectList[i].x + 50, ballRectList[i].top)
        ballleft = (ballRectList[i].left, ballRectList[i].y + 50)
        ballright = (ballRectList[i].right, ballRectList[i].y + 50)
        ballbottom = (ballRectList[i].x + 50, ballRectList[i].bottom)
        #iterating through each ball again to test collision
        for e in range(len(ballRectList)):
            #e != i to avoid a ball colliding with itself
            if(e != i):
                #second set of side vars for collision
                balltopE = (ballRectList[e].x + 50, ballRectList[e].top)
                ballleftE = (ballRectList[e].left, ballRectList[e].y + 50)
                ballrightE = (ballRectList[e].right, ballRectList[e].y + 50)
                ballbottomE = (ballRectList[e].x + 50, ballRectList[e].bottom)
                
                #this tests for collision between both balls, the reason there is 2 sections is
                #so that the balls bounce off each other properly

                #if ballI is colliding with ballE
                if ballRectList[i].collidepoint(ballleftE):
                    ballSpeedList[e][0] = -ballSpeedList[e][0]
                if ballRectList[i].collidepoint(balltopE):
                    ballSpeedList[e][1] = -ballSpeedList[e][1]                   
                if ballRectList[i].collidepoint(ballrightE):
                    ballSpeedList[e][0] = -ballSpeedList[e][0]                    
                if ballRectList[i].collidepoint(ballbottomE):
                    ballSpeedList[e][1] = -ballSpeedList[e][1]
             
                #if ballE is colliding with ballI
                if ballRectList[e].collidepoint(ballleft):
                    ballSpeedList[i][0] = -ballSpeedList[i][0]                   
                if ballRectList[e].collidepoint(balltop):
                    ballSpeedList[i][1] = -ballSpeedList[i][1]                  
                if ballRectList[e].collidepoint(ballright):
                    ballSpeedList[i][0] = -ballSpeedList[i][0]               
                if ballRectList[e].collidepoint(ballbottom):
                    ballSpeedList[i][1] = -ballSpeedList[i][1]
                    
        
        screen.blit(ballSprite, ballRectList[i])
 
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
