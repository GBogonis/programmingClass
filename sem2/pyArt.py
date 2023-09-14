#start

#import is in a try so if the import doesn't work the program will quit before it breaks
try:
    import pygame
except:
    print("could not import pygame")
    exit() 

# Define some colors (I looked up the real RGB values for the colors of the flag)
WHITE = (255, 255, 255)
BLUE = (0, 33, 71)
RED = (187,19,62)

 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1425, 714)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("The Flag")

#off-set type varible for drawing things
dif = 686

# Set variable to run loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()
screen.fill(WHITE)
# -------- Main Program Loop -----------
while not done:
    # --- Main event to break loop when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    # --- Drawing code should go here
        
        #loop for drawing the red stripes
        for dif in range(dif, -5, -110):
            pygame.draw.line(screen,(RED),(0,0+dif),(1425,0+dif), 54)

        #drawing the blue rectangle
        pygame.draw.rect(screen, (BLUE), pygame.Rect(0, 0, 590, 384))

        #drawing the white squares because stars are too hard :(
        for i in range(10, -1, -1):
            pygame.draw.rect(screen, (WHITE), pygame.Rect(63*i-100,10,30,30))
            pygame.draw.rect(screen, (WHITE), pygame.Rect(63*i-100,86,30,30))
            pygame.draw.rect(screen, (WHITE), pygame.Rect(63*i-100,2*86,30,30))
            pygame.draw.rect(screen, (WHITE), pygame.Rect(63*i-100,3*86,30,30))
            pygame.draw.rect(screen, (WHITE), pygame.Rect(63*i-100,4*86,30,30))
            
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
