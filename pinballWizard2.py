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
ball1Speed = [5,5]
ball2Speed = [5,5]
ball1Rect = ballSprite.get_rect()
ball2Rect = ballSprite.get_rect()
ball1Rect.x = random.randrange(0, screenWidth-111)
ball1Rect.y = random.randrange(0, screenHight-111)
ball2Rect.x = random.randrange(0, screenWidth-111)
ball2Rect.y = random.randrange(0, screenHight-111)

ballRectList = []
ballSpeedList = []
for i in range(3):
    ballSpeedList.append([1,1])
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
        ballRectList[i] = ballRectList[i].move(ballSpeedList[i])
        
        if ballRectList[i].left < 0 or ballRectList[i].right > screenWidth: # uses edges of ballRectList[i] surface to detect collision with screen surface
            ballSpeedList[i][0] = -ballSpeedList[i][0] # reverse horizontal speed to stay on screen
        if ballRectList[i].top < 0 or ballRectList[i].bottom > screenHight:
            ballSpeedList[i][1] = -ballSpeedList[i][1] # reverse vertical speed to stay on screen

        balltop = (ballRectList[i].x + 50, ballRectList[i].top)
        ballleft = (ballRectList[i].left, ballRectList[i].y + 50)
        ballright = (ballRectList[i].right, ballRectList[i].y + 50)
        ballbottom = (ballRectList[i].x + 50, ballRectList[i].bottom)
        for e in range(len(ballRectList)):
            if(e != i):
                balltopE = (ballRectList[e].x + 50, ballRectList[e].top)
                ballleftE = (ballRectList[e].left, ballRectList[e].y + 50)
                ballrightE = (ballRectList[e].right, ballRectList[e].y + 50)
                ballbottomE = (ballRectList[e].x + 50, ballRectList[e].bottom)
                
                if ballRectList[i].collidepoint(ballleftE):
                    ballSpeedList[e][0] = -ballSpeedList[e][0]
                    print("I collide E: left")
                if ballRectList[i].collidepoint(balltopE):
                    ballSpeedList[e][1] = -ballSpeedList[e][1]
                    print("I collide E: top")
                if ballRectList[i].collidepoint(ballrightE):
                    ballSpeedList[e][0] = -ballSpeedList[e][0]
                    print("I collide E: right")
                if ballRectList[i].collidepoint(ballbottomE):
                    ballSpeedList[e][1] = -ballSpeedList[e][1]
                    print("I collide E: bottom")
                
                if ballRectList[e].collidepoint(ballleft):
                    ballSpeedList[i][0] = -ballSpeedList[i][0]
                    print("E collide I: left")
                if ballRectList[e].collidepoint(balltop):
                    ballSpeedList[i][1] = -ballSpeedList[i][1]
                    print("E collide I: top")
                if ballRectList[e].collidepoint(ballright):
                    ballSpeedList[i][0] = -ballSpeedList[i][0]
                    print("E collide I: right")
                if ballRectList[e].collidepoint(ballbottom):
                    ballSpeedList[i][1] = -ballSpeedList[i][1]
                    print("E collide I: bottom")
            
        screen.blit(ballSprite, ballRectList[i])
 
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(100)
 
# Close the window and quit.
pygame.quit()
