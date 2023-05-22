#start
try:
    import pygame
    from pygame.locals import *
    import random
    import math
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
 
# Set variable to run loop until the user clicks the close button.
going = True
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()
 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (X, Y)
        mx, my = pygame.mouse.get_pos()
        #using fancy math stuff to get the direction that the bullet should be going
        self.dir = (mx - X, my - Y)
        length = math.hypot(*self.dir)
        
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.image = pygame.Surface((10, 5)).convert_alpha()
        self.image.fill(colors["BLACK"])
        self.rect = self.image.get_rect()

        #drawing stuff and other helpful class vars
        self.image = pygame.transform.rotate(self.image, angle)
        self.speed = 10

    def update(self):  
        #simple update function just moving the position, the colision stuff is in the enemy class
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        #simple draw function to be called after update
        self.rect = self.image.get_rect(center = self.pos)
        surf.blit(self.image, self.rect)  








shooting = False
#sprite groups
bulletGroup = pygame.sprite.Group()

# -------- Main Program Loop -----------
while going:
    # --- Main event to break loop when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if player is holding down the shoot button, shooting = true
            shooting = True
        elif event.type == pygame.MOUSEBUTTONUP:
            shooting = False
    
    #if we are shooting, fire a bullet!
    if(shooting):
        bulletGroup.add(Bullet(screenWidth/2, screenHight/2))
    # --- Game logic should go here
    
 
    # --- Drawing code should go here
    screen.fill(colors["WHITE"])
    
    bulletGroup.update()
    bulletGroup.draw(screen)
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
