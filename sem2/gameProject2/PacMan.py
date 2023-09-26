#start
try:
    import pygame
    from pygame.locals import *
except:
    print("could not import pygame")
    exit() 
    

# Define some colors
colors = {'BLACK':(0,0,0),"WHITE":(255, 255, 255),"GREEN":(0, 255, 0),"RED":(255, 0, 0),"BLUE":(0, 0, 255),"YELLOW":(255, 255, 0)}
 
pygame.init()
 
#256 × 240 pixels
# Set the width and height of the screen [width, height]
screenHight = 36*25
screenWidth = 28*25
size = (screenWidth, screenHight)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PacMan")
 
# Set variable to run loop until the user clicks the close button.
going = True
 
# Used to manage how fast the screen refreshes
clock = pygame.time.Clock()
 


class Player(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([20,20])

        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        #centerx is just to get the spawn position where I want it
        self.rect.centerx = x


        self.image.fill(colors["YELLOW"])
 
        self.powerupTimer = 0
        
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.dots = None
        self.powers = None
        global score 
        score = 0
        
 
    def changespeed(self, x, y):
        #set player speed
        self.change_x = x
        self.change_y = y
 
    def update(self):
        global score 
        if(self.powerupTimer > 0):
            #self.change_x *= 1.2
            #self.change_y *= 1.2
            self.powerupTimer -= 1

        #moving the player
        self.rect.x += self.change_x
 
        #checking collision with any objects after the movement
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        dot_hit_list = pygame.sprite.spritecollide(self, self.dots, True)
        power_hit_list = pygame.sprite.spritecollide(self, self.powers, True)

        for block in block_hit_list:
            #if we hit a wall, then be next to it not inside it
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                #same thing but other side
                self.rect.left = block.rect.right
 
        #virtical change
        self.rect.y += self.change_y
 
        #check if we hit any object after our second move
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            #same thing as before, if we hit a wall then don't do that
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        #if we made it out of the map, move to the other side, this will only happen when we go into the tunnle
        if(self.rect.x >screenWidth):
            self.rect.x = 10
        if(self.rect.x < 0):
            self.rect.x = screenWidth-10

        #code for eating the dots and powerups
        for dot in dot_hit_list:
            dot_hit_list.remove(dot)
            score += 100
        for power in power_hit_list:
            power_hit_list.remove(power)
            self.powerupTimer = 50
            score += 1000


class mapObject(pygame.sprite.Sprite):

    def __init__(self,type, x, y):
        #call sprite constructor
        super().__init__()

        #depending on the type thats passed in, the result is a different map element (wall, dot, powerup)
        #this was better than having 3 different classes for each
        if(type == 'w'):
            #making a simple blue 25 by 25 wall
            self.image = pygame.Surface([25, 25])
            self.image.fill(colors["BLUE"])
        elif(type == 'd'):
            #making a dot that can be eaten by the player
            self.image = pygame.Surface([10, 10])
            self.image.fill(colors["WHITE"])
        elif(type == 'p'):
            #making a power up for the player to eat 
            self.image = pygame.Surface([15, 15])
            self.image.fill(colors["WHITE"])

        #defining our x and y cords
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

#start of ghost class: deprecated
'''
class Ghost(pygame.sprite.Sprite):
    def __init__(self,color):
        super.__init__()

        self.image = pygame.surface([20,20])
        self.image.fill(colors[color])
        self.rect = self.image.get_rect()
        self.rect.y = screenHight/2
        self.rect.x = screenWidth/2

'''
#list to hold every instance of every object, pretty much just to be displayed
all_sprite_list = pygame.sprite.Group()
 
#lists for each type of object in the game
wall_list = pygame.sprite.Group()
power_list = pygame.sprite.Group()
dot_list = pygame.sprite.Group()


levelText = open(r'C:\Users\George.Bogonis\Documents\GitHub\programmingClass\sem2\gameProject2\level.txt')

#level constructor:
#I have a text file where I lay out the map by using characters (w = wall, d = dot, p = powerup)
#This section will go though each line and each character in that line a place the corrispondng object in that space
#this was a solution to the problem of trying to lay out each block of the map by hand, it would have taken for ever,
# and it would have been unreadable to anyone who tried to understand which block corrisponded to what section of the map
#this is a elegant solution to a problem that solves every issue I had, and when I got it working I was very proud of myself :)

#vars to keep track
currentRow = 0
currentBlock = 0
#going through each line in the text file
for row in levelText:
 currentBlock = 0
 currentRow +=1
 #for each 'block' or character in each line
 for block in row:
    if(block == 'w'):
        mapElement = mapObject('w',currentBlock*25,currentRow*25)
        wall_list.add(mapElement)
        all_sprite_list.add(mapElement)
    if(block == "d"):
        mapElement = mapObject('d',(currentBlock*25)+7,(currentRow*25)+7)
        dot_list.add(mapElement)
        all_sprite_list.add(mapElement)
    if(block == 'p'):
        mapElement = mapObject('p',currentBlock*25+5,currentRow*25+5)
        power_list.add(mapElement)
        all_sprite_list.add(mapElement)
    currentBlock +=1
 
#making the (only) player object and setting the vars 
player = Player(screenWidth/2, (25*27))
player.walls = wall_list
player.dots = dot_list
player.powers = power_list
all_sprite_list.add(player)

#font for score text 
textFont = pygame.font.Font('freesansbold.ttf', 32)

#time keeping
secondsLeft = 3000
# -------- Main Program Loop -----------
going = True
 
while going:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
            #movement keys for the player
        elif event.type == pygame.KEYDOWN:
            #if, no active powerup than normal speed, else than super speed
            if event.key == pygame.K_LEFT:
                if(player.powerupTimer > 0):
                    player.changespeed(-7, 0)
                else:
                    player.changespeed(-5, 0)
            if event.key == pygame.K_RIGHT:
                if(player.powerupTimer > 0):
                    player.changespeed(7, 0)
                else:
                    player.changespeed(5, 0)
            if event.key == pygame.K_UP:
                if(player.powerupTimer > 0):
                    player.changespeed(0, -7)
                else:
                    player.changespeed(0, -5)
            if event.key == pygame.K_DOWN:
                if(player.powerupTimer > 0):
                    player.changespeed(0, 5)
                else:
                    player.changespeed(0,7)

    #updating all sprites 
    all_sprite_list.update()
 
    #resetting the screen to avoid trails
    screen.fill(colors["BLACK"])
 
    #drawing all sprites 
    all_sprite_list.draw(screen)
    if(secondsLeft > 0 and len(dot_list) != 0 and len(power_list) != 0):
        #you have time and dots left, game is going
        #score text setup
        scoreText = textFont.render('Score: ' + str(score),True, (255, 255, 255))
        scoreTextRect = scoreText.get_rect()
        screen.blit(scoreText, (10,10))

        timeText = textFont.render('Time left: ',True, (255, 255, 255))
        timeText2 = textFont.render(str(secondsLeft),True,(255, 255, 255))
        timeTextRect = timeText.get_rect()
        screen.blit(timeText, (25*11,25*17))
        screen.blit(timeText2, (25*13-10,25*19-2))
        #updating the timer, only if the game is going
        secondsLeft -= 1
    elif(len(dot_list) == 0 and len(power_list) == 0 and secondsLeft > 0):
        #if you have no dots or powerups left and you have time left, you win
        timeText = textFont.render('You',True, (255, 255, 255))
        timeText2 = textFont.render('Win',True,(255, 255, 255))
        timeTextRect = timeText.get_rect()
        screen.blit(timeText, (25*11,25*17))
        screen.blit(timeText2, (25*14-10,25*19-2))
    else:
        #game over text
        timeText = textFont.render('Game',True, (255, 255, 255))
        timeText2 = textFont.render('Over',True,(255, 255, 255))
        timeTextRect = timeText.get_rect()
        screen.blit(timeText, (25*11,25*17))
        screen.blit(timeText2, (25*14-10,25*19-2))


    #updating screen stuff
    pygame.display.flip()
    print(secondsLeft)
    clock.tick(30)
 
pygame.quit()