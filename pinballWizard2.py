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
for i in range(2):
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
                if ballRectList[i].collidepoint(balltopE):
                    ballSpeedList[e][1] = -ballSpeedList[e][1]
                if ballRectList[i].collidepoint(ballrightE):
                    ballSpeedList[e][0] = -ballSpeedList[e][0]
                if ballRectList[i].collidepoint(ballbottomE):
                    ballSpeedList[e][1] = -ballSpeedList[e][1]
                
                if ballRectList[e].collidepoint(ballleft):
                    ballSpeedList[i][0] = -ballSpeedList[i][0]
                if ballRectList[e].collidepoint(balltop):
                    ballSpeedList[i][1] = -ballSpeedList[i][1]
                if ballRectList[e].collidepoint(ballright):
                    ballSpeedList[i][0] = -ballSpeedList[i][0]
                if ballRectList[e].collidepoint(ballbottom):
                    ballSpeedList[i][1] = -ballSpeedList[i][1]
        screen.blit(ballSprite, ballRectList[i])


    '''
    ball1Rect = ball1Rect.move(ball1Speed)
    if ball1Rect.left < 0 or ball1Rect.right > screenWidth: # uses edges of ball1Rect surface to detect collision with screen surface
        ball1Speed[0] = -ball1Speed[0] # reverse horizontal speed to stay on screen
    if ball1Rect.top < 0 or ball1Rect.bottom > screenHight:
        ball1Speed[1] = -ball1Speed[1] # reverse vertical speed to stay on screen

    ball2Rect = ball2Rect.move(ball2Speed)
    if ball2Rect.left < 0 or ball2Rect.right > screenWidth: # uses edges of ball2Rect surface to detect collision with screen surface
        ball2Speed[0] = -ball2Speed[0] # reverse horizontal speed to stay on screen
    if ball2Rect.top < 0 or ball2Rect.bottom > screenHight:
        ball2Speed[1] = -ball2Speed[1] # reverse vertical speed to stay on screen
    
    
    ball1top = (ball1Rect.x + 50, ball1Rect.top)
    ball1left = (ball1Rect.left, ball1Rect.y + 50)
    ball1right = (ball1Rect.right, ball1Rect.y + 50)
    ball1bottom = (ball1Rect.x + 50, ball1Rect.bottom)
    
    ball2top = (ball2Rect.x + 50, ball2Rect.top)
    ball2left = (ball2Rect.left, ball2Rect.y + 50)
    ball2right = (ball2Rect.right, ball2Rect.y + 50)
    ball2bottom = (ball2Rect.x + 50, ball2Rect.bottom)
    
    
    if ball1Rect.collidepoint(ball2left):
        ball2Speed[0] = -ball2Speed[0]
    if ball1Rect.collidepoint(ball2top):
        ball2Speed[1] = -ball2Speed[1]
    if ball1Rect.collidepoint(ball2right):
        ball2Speed[0] = -ball2Speed[0]
    if ball1Rect.collidepoint(ball2bottom):
        ball2Speed[1] = -ball2Speed[1]
    
    if ball2Rect.collidepoint(ball1left):
        ball1Speed[0] = -ball1Speed[0]
    if ball2Rect.collidepoint(ball1top):
        ball1Speed[1] = -ball1Speed[1]
    if ball2Rect.collidepoint(ball1right):
        ball1Speed[0] = -ball1Speed[0]
    if ball2Rect.collidepoint(ball1bottom):
        ball1Speed[1] = -ball1Speed[1]
    '''
    '''
    collided = False
    if ball1Rect.collidepoint(ball2left) and collided == False:
        ball2Speed[0] = -ball2Speed[0]
        collided = True
    if ball1Rect.collidepoint(ball2top) and collided == False:
        ball2Speed[1] = -ball2Speed[1]
        collided = True
    if ball1Rect.collidepoint(ball2right) and collided == False:
        ball2Speed[0] = -ball2Speed[0]
        collided = True
    if ball1Rect.collidepoint(ball2bottom) and collided == False:
        ball2Speed[1] = -ball2Speed[1]
        collided = True
    
    if ball2Rect.collidepoint(ball1left) and collided == False:
        ball1Speed[0] = -ball1Speed[0]
        collided = True
    if ball2Rect.collidepoint(ball1top) and collided == False:
        ball1Speed[1] = -ball1Speed[1]
        collided = True
    if ball2Rect.collidepoint(ball1right) and collided == False:
        ball1Speed[0] = -ball1Speed[0]
        collided = True
    if ball2Rect.collidepoint(ball1bottom) and collided == False:
        ball1Speed[1] = -ball1Speed[1]
        collided = True




    '''
    
    #screen.blit(ballSprite, ball1Rect)
    #screen.blit(ballSprite,ball2Rect)
           
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)
 
# Close the window and quit.
pygame.quit()
