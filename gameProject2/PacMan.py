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
colors = {'BLACK':(0,0,0),"WHITE":(255, 255, 255),"GREEN":(0, 255, 0),"RED":(255, 0, 0),"BLUE":(0, 0, 255)}
 
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
        self.image = pygame.Surface([25, 25])

        self.image.fill(colors["RED"])
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x = x
        self.change_y = y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
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

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(colors["BLUE"])
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 


# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
#walls
widthUnit=15
PosUnit=25
#left wall 1
wall = Wall(0, 75, 25, 250)
wall_list.add(wall)
all_sprite_list.add(wall)

#right wall 2
wall = Wall(screenWidth-25, 75, 25, 250)
wall_list.add(wall)
all_sprite_list.add(wall)

#left tunnel
wall = Wall(0, 25*17, 25*6, 25)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 25*19, 25*6, 25)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 25*13, 25*6, 25)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 25*23, 25*6, 25)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(25*5, 25*13, 25, 25*5)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(25*5, 25*19, 25, 25*5)
wall_list.add(wall)
all_sprite_list.add(wall)

#left wall 2
wall = Wall(0, 23*25, 25, 300)
wall_list.add(wall)
all_sprite_list.add(wall)

#right wall 2
wall = Wall(screenWidth-25, 22*25, 25, 300)
wall_list.add(wall)
all_sprite_list.add(wall)

#top wall
wall = Wall(0, 75, screenWidth, 25)
wall_list.add(wall)
all_sprite_list.add(wall)

#bottom wall
wall = Wall(0, screenHight-75, screenWidth, 25)
wall_list.add(wall)
all_sprite_list.add(wall)



 


# Create the player paddle object
player = Player(screenWidth/2, screenHight/2)
player.walls = wall_list

all_sprite_list.add(player)
# -------- Main Program Loop -----------
going = True
 
while going:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, -3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

    all_sprite_list.update()
 
    screen.fill(colors["BLACK"])
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()