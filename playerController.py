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
RED = (150, 0, 0)
BLUE = (0, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screenWidth = 612
screenHight = 383
size = (screenWidth, screenHight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Pygame")
oceanBackground = pygame.image.load("istockphoto-1215044710-612x612.jpg")

#game variables/functions
fishPos = (350,250)
otherFishX = 350
otherFishY = 250

#fish function
def drawFish(X, Y):
    X = int(X)
    Y = int(Y)
    bodyWide = 70
    bodyTall = 40
    #body
    pygame.draw.ellipse(screen,RED,[X-(bodyWide/2),Y-(bodyTall/2),bodyWide,bodyTall],0)
    #eye
    pygame.draw.circle(screen,BLACK,[X+15,Y],5,0)
    #tail fin thing 
    pygame.draw.polygon(screen,RED,((X-(bodyWide/2),Y), (X-50,Y-20), (X-50,Y+20)),0)
 
# Set variable to run loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event to break loop when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            key_pressed_is = pygame.key.get_pressed()
        else:
            key_pressed_is = 'none'
        
 
    # --- Game logic should go here
    #logic to not let the fish go off the screen
    if(otherFishX+40 > screenWidth):
        otherFishX = screenWidth-35
    elif(otherFishX-50 < 0):
        otherFishX = 50
    if(otherFishY+20 > screenHight):
        otherFishY = screenHight-20
    elif(otherFishY-20 < 0):
        otherFishY = 20
 
    # --- Drawing code should go here
    screen.blit(oceanBackground,(0,0))
    #fish 1
    drawFish(fishPos[0],fishPos[1])
    #fish 2
    drawFish(otherFishX,otherFishY)
    
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    #updating the position of the fish
    fishPos = pygame.mouse.get_pos()
    try:
        if key_pressed_is[K_LEFT]:
            otherFishX -= 8
        elif key_pressed_is[K_RIGHT]:
            otherFishX += 8
        if key_pressed_is[K_UP]:
            otherFishY -= 8
        elif key_pressed_is[K_DOWN]:
            otherFishY += 8
    except:
        otherFishX = otherFishX
        otherFishY = otherFishY

 
# Close the window and quit.
pygame.quit()
