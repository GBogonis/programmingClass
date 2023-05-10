try:
    import pygame
    from pygame.locals import *
    import random
    import math
except:
    print("could not import pygame")
    exit() 
    
# Define some colors
colors = {'BLACK':(0,0,0),"WHITE":(255, 255, 255),"GREEN":(0, 255, 0),"RED":(255, 0, 0),"BLUE":(0, 0, 255)}
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screenWidth = 1000
screenHight = 700
screenSize = (screenWidth, screenHight)
screen = pygame.display.set_mode(screenSize)

 
pygame.display.set_caption("My Pygame")

 
# Set variable to run loop until the user clicks the close button.
going = True
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()


class Bullet:
    def __init__(self, X, Y):
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

        #drawing stuff and other helpful class vars
        self.bullet_rect = Rect
        self.bullet = pygame.Surface((10, 5)).convert_alpha()
        self.bullet.fill(colors["BLACK"])
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 10

    def update(self):  
        #simple update function just moving the position, the colision stuff is in the enemy class
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        #simple draw function to be called after update
        self.bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, self.bullet_rect)  

class Enemy:
    def __init__(self, X, Y, rect):
        #the class is created with the start position as the argument so we don't have to worry about that here
        self.enemypos = (X, Y)
        
        #setting the init direction
        self.setDir()
        #other helpful vars
        self.enemyRect = rect
        self.speed = 1
        self.health = 10
        self.alive = True

    def setDir(self):
        #code to get the direction the enemy should be moving in (sililar to the bullet code)
        #note: the player will always be at the center of the screen so we can just use the screen values divided by 2
        self.enemydir = (screenWidth/2 - self.enemypos[0], screenHight/2 - self.enemypos[1])
        
        length = math.hypot(*self.enemydir)
        if length == 0.0:
            self.enemydir = (0, -1)
        else:
            self.enemydir = (self.enemydir[0]/length, self.enemydir[1]/length)
    
    def setSpeed(self, newSpeed):
        self.speed = newSpeed
    
    def update(self, bulletList):
        Xdif = (self.enemypos[0]-(screenWidth/2))
        Ydif = (self.enemypos[1]-(screenHight/2))

        #I could just call "setDir()" all the time but I like the movement better this way
        if(Xdif >25 and self.enemydir[0]>0):
            self.setDir()
        if(Ydif >25 and self.enemydir[1]>0):
            self.setDir()
        if(Xdif <-25 and self.enemydir[0]<0):
            self.setDir()
        if(Ydif <-25 and self.enemydir[1]<0):
            self.setDir()
        
        #moving the enemy
        self.enemypos = (self.enemypos[0]+self.enemydir[0]*self.speed, 
                    self.enemypos[1]+self.enemydir[1]*self.speed)

        #interaction with bullet stuff
        #subtracts the amout of bullets colliding from the total health
        shots = self.enemyRect.collidelistall(bulletList)
        damage = len(shots)
        self.health -= damage
        #if dead, don't be alive
        if(self.health <= 0):
            self.alive = False

    def draw(self, surf):
        #if not dead, exist!
        if(self.alive):
            self.enemyRect.center = (self.enemypos)
            pygame.draw.ellipse(surf,colors["RED"],self.enemyRect)

    def getAlive(self):
        return self.alive

class player:
    #simple player class, tbh not really needed but its fun
    def __init__(self, pos, rect):
        self.playerPos = pos
        self.HP = 100
        self.playerRect = rect
    
    def update(self, enemyRectList, enemyAliveList):
        for i in range(len(enemyRectList)):
            if(enemyAliveList[i] == True and self.playerRect.colliderect(enemyRectList[i])):
                self.HP -= 1

    def draw(self, surf):
        self.playerRect.center = (self.playerPos)
        pygame.draw.ellipse(surf,colors["BLUE"],self.playerRect)


#game vars
bullets = []
enemyList = []
attacking = False
roundNum = 1
mPlayer = player((screenWidth/2, screenHight/2), Rect(screenWidth/2, screenHight/2, 60, 60))
font = pygame.font.Font('freesansbold.ttf', 32)


def spawnEnemies(num):
    #random spawn location code for enemies
    for i in range(num):
        ranX = random.randrange(0,screenWidth)
        ranY = random.randrange(0,screenHight)
        if(ranX > 50 and ranX < screenWidth-50):
            if(random.random() == 1):
                ranY = 0
            else:
                ranY = screenHight
        enemyList.append(Enemy(ranX,ranY,Rect(200, 500, 50, 50)))

spawnEnemies(5)
movingUp = False
# -------- Main Program Loop -----------
while going:
    # --- Main event to break loop when user quits
    move_ticker = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        if event.type == pygame.MOUSEBUTTONUP:
            bullets.append(Bullet(*mPlayer.playerPos))
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movingUp = True
        else:
            movingUp = False
        '''
    location = 0
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        if move_ticker == 0:
            move_ticker = 10
            location -= 1
            if location == -1:
                location = 0
    if keys[K_RIGHT]:
        if move_ticker == 0:   
            move_ticker = 10     
            location+=1
            if location == 5:
                location = 4
    
    if(location == 1):
        print('left')
    elif(location == -1):
        print('right')

    if move_ticker > 0:
        move_ticker -= 1
    #main game code
    screen.fill(colors["WHITE"])
    bulletRectlist = []
    enemyRectList = []
    if(mPlayer.HP > 0):
        HPText = font.render('HP:' + str(mPlayer.HP),True, (0, 0, 0))

        RoundText = font.render('Round: ' + str(roundNum),True, (0, 0, 0))
        screen.blit(HPText,(10,10))
        screen.blit(RoundText,(10,screenHight-30))

        #bullet code
        for bullet in bullets:
            bullet.update()
            bullet.draw(screen)
            bulletRectlist.append(bullet.bullet_rect)
        
        #enemy code
        enemyAliveList = []
        for enemy in enemyList:
            enemy.setSpeed(roundNum)
            enemy.update(bulletRectlist)
            enemy.draw(screen)
            enemyAliveList.append(enemy.getAlive())
            enemyRectList.append(enemy.enemyRect)


        
        if True not in enemyAliveList:
            roundNum += 1
            spawnEnemies(4+roundNum)
            mPlayer.HP += 50
        
        
        #draw player
        mPlayer.update(enemyRectList,enemyAliveList)
        mPlayer.draw(screen)
    else:
        endText1 = font.render("Game over!", True, (0, 0, 0))
        endRect1 = endText1.get_rect()
        endRect1.center = (screenWidth / 2, screenHight / 2)
        endText2 = font.render('You survived ' + str(roundNum) + ' round(s)',True, (0,0,0))
        endRect2 = endText2.get_rect()
        endRect2.center = (screenWidth / 2, (screenHight / 2)+30)
        screen.blit(endText1, endRect1)
        screen.blit(endText2, endRect2)

    
    # --- Go ahead and refresh the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    mousePos = pygame.mouse.get_pos()
 
# Close the window and quit.
pygame.quit()
