try:
    import pygame
    from pygame.locals import *
    import random
    import math
except:
    print("could not import pygame 1")
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
screenWidth = 1000
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
    def __init__(self, X, Y):
        self.pos = (X, Y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - X, my - Y)
        length = math.hypot(*self.dir)
        self.bullet_rect = Rect
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((10, 5)).convert_alpha()
        self.bullet.fill(colors["BLACK"])
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 10

    def update(self):  
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        self.bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, self.bullet_rect)  

class Enemy:
    def __init__(self, X, Y, rect):
        self.enemyRect = rect
        self.enemypos = (X, Y)
        self.enemydir = (screenWidth/2 - X, screenHight/2 - Y)
        
        length = math.hypot(*self.enemydir)
        if length == 0.0:
            self.enemydir = (0, -1)
        else:
            self.enemydir = (self.enemydir[0]/length, self.enemydir[1]/length)
        #angle = math.degrees(math.atan2(-self.enemydir[1], self.enemydir[0]))
        self.speed = 5
        self.health = 10
        self.alive = True
    
    def update(self, bulletList):
        #Xdis = math.hypot(self.enemypos[0],screenWidth/2)
        #Ydis = math.hypot(self.enemypos[1],screenHight/2)
        Xdif = (self.enemypos[0]-(screenWidth/2))
        Ydif = (self.enemypos[1]-(screenHight/2))
        print(Xdif,Ydif)
        #todo: figure out you to turn around
        if(Xdif >25 and self.enemydir[0]>0):
            print('turn around X')
        if(Ydif >25 and self.enemydir[1]>0):
            print('turn around Y')
        if(Xdif <-25 and self.enemydir[0]<0):
            print('turn around X')
        if(Ydif <-25 and self.enemydir[1]<0):
            print('turn around Y')
        
        self.enemypos = (self.enemypos[0]+self.enemydir[0]*self.speed, 
                    self.enemypos[1]+self.enemydir[1]*self.speed)

        #self.enemypos = (self.enemypos[0]-Xdif, self.enemypos[1]-Ydif)
        #self.enemypos = (self.enemypos[0] + self.enemydir[0], self.enemypos[1] + self.enemydir[1])
        #print(self.enemypos)
        shots = self.enemyRect.collidelistall(bulletList)
        damage = len(shots)
        self.health -= damage
        if(self.health <= 0):
            self.alive = False

    def draw(self, surf):
        if(self.alive):
            self.enemyRect.center = (self.enemypos)
            pygame.draw.ellipse(surf,colors["RED"],self.enemyRect)

class player:
    def __init__(self,pos):
        self.playerPos = pos

        

    

bullets = []

pos = (250, 250)
enemyList = []
for i in range(5):
    ranX = random.randrange(0,screenWidth)
    ranY = random.randrange(0,screenHight)
    if(ranX > 50 and ranX < screenWidth-50):
        if(random.random() == 1):
            ranY = 0
        else:
            ranY = screenHight
    enemyList.append(Enemy(ranX,ranY,Rect(200, 500, 50, 50)))
mEnemy = Enemy(screenWidth,screenHight,Rect(200, 500, 50, 50))
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
    bulletRectlist = []
    #bullet code
    for bullet in bullets:
        bullet.update()
        bullet.draw(screen)
        bulletRectlist.append(bullet.bullet_rect)
    '''
    for enemy in enemyList:
        enemy.update(bulletRectlist)
        enemy.draw(screen)'''
    mEnemy.update(bulletRectlist)
    mEnemy.draw(screen)

    #draw player
    pygame.draw.circle(screen,(BLUE),(playerPos),30)
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)
    mousePos = pygame.mouse.get_pos()
 
# Close the window and quit.
print('quit')
pygame.quit()
