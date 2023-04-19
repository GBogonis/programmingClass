#start
#imports
try:
    import pygame
    from pygame.locals import *
    import random
except:
    print("could not import pygame")
    exit() 
    
#color dictionary because python doesn't have enums like java
colors = {'BLACK':(0,0,0),"WHITE":(255, 255, 255),"GREEN":(0, 255, 0),"RED":(255, 0, 0),"BLUE":(0, 0, 255)}
 
#pygame start
pygame.init()
 
# Set the width and height of the screen [width, height]
screenHight = 700
screenWidth = 1000
size = (screenWidth, screenHight)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Pygame")


# load ball image
ballSprite = pygame.image.load("intro_ball.gif")
#setup vars for balls
ballRectList = []
ballSpeedList = []
#'ballRealList is for when the balls get clicked we know they should be gone
ballRealList = []
#making a new set of vars for each ball and adding to the list
for i in range(5):
    ballSpeedList.append([5,5])
    ballRect = ballSprite.get_rect()
    ballRect.x = random.randrange(0, screenWidth-111)
    ballRect.y = random.randrange(0, screenHight-111)
    ballRectList.append(ballRect)
    ballRealList.append(True)

#game vars
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

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
        if event.type == pygame.MOUSEBUTTONUP:
            clicking = True
        else:
            clicking = False
 

    # --- Game logic should go here
    screen.fill(colors["BLACK"])#reset the screen to avoid trails
    #going though each ball in the ball list
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
            #e != i to avoid a ball colliding with itself, and checking that both balls are real so we don't collide with nothing
            if(e != i and (ballRealList[e] == True and ballRealList[i] == True)):
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
        
        if(clicking and (mousePos[0] >= ballleft[0] and mousePos[0] <= ballright[0]) and (mousePos[1] >= balltop[1] and mousePos[1] <= ballbottom[1])):
            ballRealList[i] = False
        
        if(ballRealList[i]):
            #adding the ball to the screen
            screen.blit(ballSprite, ballRectList[i])
    #score code
    score = 0
    #I had to do it this way to avoid 1 ball being scored many times
    for i in ballRealList:
        if(i == False):
            score += 1
    scoreText = font.render('Score:' + str(score), True, (255, 255, 255))

    #endgame text, I made it a rect to center the text easily
    winText = font.render("You win! Your score was:"+ str(score), True, (255, 255, 255))
    winRect = winText.get_rect()
    winRect.center = (screenWidth / 2, screenHight / 2)

    #checking if the game is over
    if True not in ballRealList:
        screen.blit(winText,winRect)
    else:
        screen.blit(scoreText,(10,10))

    pygame.display.flip()#update screen
    mousePos = pygame.mouse.get_pos()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

#I wanted to do more with this but the collision took longer than expected and I'm still not entirely happy with it
#there might have been a better way to do the collision but I'm already late with this project