try:
    import pygame
    from pygame.locals import *
    import random
    import enemy
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
screenWidth = 700
screenHight = 700
screenSize = (screenWidth, screenHight)
screen = pygame.display.set_mode(screenSize)
#screen = pygame.display.set_mode(screenSize, pygame.FULLSCREEN)
 
pygame.display.set_caption("My Pygame")

 
# Set variable to run loop until the user clicks the close button.
going = True
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()

playerPosX = screenWidth/2
playerPosY = screenHight/2
playerPos = playerPosX, playerPosY
playerHealth = 250

attacking = False

class Bullet:
    def __init__(self, x, y):
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((10, 5)).convert_alpha()
        self.bullet.fill(colors["RED"])
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 2

    def update(self):  
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, bullet_rect)  


bullets = []
pos = (250, 250)
# -------- Main Program Loop -----------
while going:
    # --- Main event to break loop when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
            print('quiting')
        if event.type == pygame.MOUSEBUTTONUP:
            bullets.append(Bullet(*playerPos))
        

    # --- Game logic should go here
    

    
    # --- Drawing code should go here
    screen.fill(colors["WHITE"])
   
    #bullet code
    for bullet in bullets:
        bullet.update()
        bullet.draw(screen)
    #draw player
    pygame.draw.circle(screen,(BLUE),(playerPos),30)
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    mousePos = pygame.mouse.get_pos()
 
# Close the window and quit.
print('quit')
pygame.quit()
exit()
