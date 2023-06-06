#start
try:
    import pygame
    from pygame.locals import *
    import random
    from math import atan, cos, sin
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
        self.image = pygame.Surface([20, 20])

        self.image.fill(colors["YELLOW"])
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.rect.centerx = x
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.dots = None
        global score 
        score = 0
        
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x = x
        self.change_y = y
 
    def update(self):
        global score 
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        dot_hit_list = pygame.sprite.spritecollide(self, self.dots, True)

        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        if(self.rect.x >screenWidth):
            self.rect.x = 10
        if(self.rect.x < 0):
            self.rect.x = screenWidth-10
        for dot in dot_hit_list:

            dot_hit_list.remove(dot)
            score += 100

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([25, 25])
        self.image.fill(colors["BLUE"])
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Dot(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([10, 10])
        self.image.fill(colors["WHITE"])
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

dot_list = pygame.sprite.Group()


levelText = open(r'c:\Users\George.Bogonis\Documents\GitHub\programmingClass\gameProject2\level.txt','r')

currentRow = 0
currentBlock = 0
for row in levelText:
 currentBlock = 0
 currentRow +=1
 for block in row:
    if(block == 'w'):
        wall = Wall(currentBlock*25,currentRow*25)
        wall_list.add(wall)
        all_sprite_list.add(wall)
    if(block == "d"):
        dot = Dot((currentBlock*25)+7,(currentRow*25)+7)
        dot_list.add(dot)
        all_sprite_list.add(dot)
    currentBlock +=1
 
# Create the player paddle object
player = Player(screenWidth/2, (25*27))
player.walls = wall_list
player.dots = dot_list
all_sprite_list.add(player)
# -------- Main Program Loop -----------
going = True
 
while going:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(5, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, -5)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, 5)

    all_sprite_list.update()
 
    screen.fill(colors["BLACK"])
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(30)
 
pygame.quit()