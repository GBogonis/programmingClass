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
ballListSpeed = []
ballPos = []
ballRect = []
ball1pos = [random.randrange(0, screenWidth-111),random.randrange(0, screenHight-111)]
ball2pos = [random.randrange(0, screenWidth-111),random.randrange(0, screenHight-111)]
ball1Speed = [5,5]
ball2Speed = [5,5]

'''
ballPos.append([random.randrange(0, screenWidth-111),random.randrange(0, screenHight-111)])
ballListSpeed.append([5,5])
ballRect.append(ballSprite.get_rect())
''' 
player_rect = Rect(200, 500, 50, 50)

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
    ball1Rect = ballSprite.get_rect()
    ball1RectTop = ballSprite.get_rect().midtop
    ball1RectBottom = ballSprite.get_rect().midbottom
    ball1RectLeft = ballSprite.get_rect().midleft
    ball1RectRight = ballSprite.get_rect().midright
    ball2RectTop = ballSprite.get_rect().midtop
    ball2RectBottom = ballSprite.get_rect().midbottom
    ball2RectLeft = ballSprite.get_rect().midleft
    ball2RectRight = ballSprite.get_rect().midright
    ball1Rect.move(ball1Speed[0],ball1Speed[1])
    '''
    #ball1pos[0] += ball1Speed[0]
    ball1pos[1] += ball1Speed[1]
    ball2pos[0] += ball2Speed[0]
    ball2pos[1] += ball2Speed[1]
    '''
    screen.blit(ballSprite, (ball1pos))
    screen.blit(ballSprite,(ball2pos))
    print(ball1RectTop)
    '''
    #x
    if ball1RectTop < 0 or ball1RectBottom > screenWidth-111: # uses the position of the ball to detect collision with screen surface with a offset to acount for the image size
        ballListSpeed[0] = -ballListSpeed[0]
    #y
    if ball1RectLeft < 0 or ball1RectRight > screenHight-111:
        ballListSpeed[1] = -ballListSpeed[1] # reverse vertical speed to stay on screen
    '''


    '''
    for i in range(len(ballPos)):
        ballPos[i][0] += ballListSpeed[i][0]
        ballPos[i][1] += ballListSpeed[i][1]
        screen.blit(ballSprite,(ballPos[i][0],ballPos[i][1]))
        #border collision 
        #x
        if ballPos[i][0] < 0 or ballPos[i][0] > screenWidth-111: # uses the position of the ball to detect collision with screen surface with a offset to acount for the image size
            ballListSpeed[i][0] = -ballListSpeed[i][0]
        #y
        if ballPos[i][1] < 0 or ballPos[i][1] > screenHight-111:
            ballListSpeed[i][1] = -ballListSpeed[i][1] # reverse vertical speed to stay on screen
        

        
        #ball to ball collision
        for e in range(len(ballPos)):
            #iterating though ball list again for collision
            #the purpose of 'e' is to be 'i' but it skips the ball we are already going through
            #print('in loop')
            if(i != e):
                collide = pygame.Rect.colliderect(ballRect[i],ballRect[e])
                if(pygame.Rect.colliderect(ballRect[i],ballRect[e])):
                    print('collide')
                else:
                    print('not collide')
                
                #note: try this way
                #https://www.geeksforgeeks.org/adding-collisions-using-pygame-rect-colliderect-in-pygame/?ref=rp
                print('collision running')
                balltop = (ballRect[e].x, ballRect[e].top)
                ballleft = (ballRect[e].left, ballRect[e].y)
                ballright = (ballRect[e].right, ballRect[e].y)
                ballbottom = (ballRect[e].x, ballRect[e].bottom)
                
                # check collision
                if ballRect[i].collidepoint(ballleft):
                    ballListSpeed[i][0] = -ballListSpeed[i][0]
                if ballRect[i].collidepoint(balltop):
                    ballListSpeed[i][1] = -ballListSpeed[i][1]
                if ballRect[i].collidepoint(ballright):
                    ballListSpeed[i][0] = -ballListSpeed[i][0]
                if ballRect[i].collidepoint(ballbottom):            
                    ballListSpeed[i][1] = -ballListSpeed[i][1]
                '''
                
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)
 
# Close the window and quit.
pygame.quit()
