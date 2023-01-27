try:
    import pygame
except:
    print("could not import pygame")
    exit() 

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Art")

Pos = 360
 
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
 
    # --- Game logic should go here

    # --- Drawing code should go here
        screen.fill(BLACK)
        for Pos in range(Pos, 0, 15):
            pygame.draw.line(screen,(BLUE),(Pos,Pos+50),70, 0)
        pygame.draw.line(screen,(BLUE),(Pos,250),70, 0)
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
