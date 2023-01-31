try:
    import pygame
except:
    print("could not import pygame")
    exit() 

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 33, 71)
RED = (187,19,62)

 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1425, 714)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Art")

Pos = 360
dif = 686
count = 0
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
        
        for dif in range(dif, -5, -110):
            count += 1
            pygame.draw.line(screen,(RED),(0,0+dif),(1425,0+dif), 54)
        pygame.draw.rect(screen, (BLUE), pygame.Rect(0, 0, 590, 384))
            
        

        #pygame.draw.line(screen,(BLUE),(Pos,250),70, 0)
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
    print(count)
    count = 0
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
