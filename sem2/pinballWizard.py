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
for i in range(2):
    ballPos.append([random.randrange(0, screenWidth-111),random.randrange(0, screenHight-111)])
    ballListSpeed.append([5,5])
    ballRect.append(ballSprite.get_rect())
  

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
    for i in range(len(ballPos)):
        '''
        pygame.draw.line(screen,colors["WHITE"],ballPos[i],(ballPos[i][0]+111,ballPos[i][1]))
        pygame.draw.line(screen,colors["WHITE"],(ballPos[i][0],ballPos[i][1]+111),(ballPos[i][0]+111,ballPos[i][1]+111))
        pygame.draw.line(screen,colors["WHITE"],ballPos[i],(ballPos[i][0],ballPos[i][1]+111))
        pygame.draw.line(screen,colors["WHITE"],(ballPos[i][0]+111,ballPos[i][1]),(ballPos[i][0]+111,ballPos[i][1]+111))
        '''

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
                
                #print('ball i:',ballPos[i][0], 'ball e:', ballPos[e][0])
                #print('diff:', ballPos[i][1] - ballPos[e][1])
                
                if((ballPos[i][0]+105 >= ballPos[e][0] and ballPos[i][0]-105 <= ballPos[e][0]) and (ballPos[i][1]+105 >= ballPos[e][1] and ballPos[i][1]-105 <= ballPos[e][1])):
                    ballListSpeed[i][0] = -ballListSpeed[i][0]
                    ballListSpeed[e][0] = -ballListSpeed[e][0]
                    ballListSpeed[i][1] = -ballListSpeed[i][1]
                    ballListSpeed[e][1] = -ballListSpeed[e][1]

                '''
                if(ballPos[i][0]+111 >= ballPos[e][0] and ballPos[i][0]-111 <= ballPos[e][0]):
                    ballListSpeed[i][0] = -ballListSpeed[i][0]
                    ballListSpeed[e][0] = -ballListSpeed[e][0]
                    
                    print('collide')
                
                if(ballPos[i][1]+111 >= ballPos[e][1] and ballPos[i][1]-111 <= ballPos[e][1]):
                    ballListSpeed[i][1] = -ballListSpeed[i][1]
                    ballListSpeed[e][1] = -ballListSpeed[e][1]
                    print('collide')

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
