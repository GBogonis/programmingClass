# extended from this first tutorial from:
# https://www.pygame.org/docs/tut/PygameIntro.html
# adding a second object for collision
# using collidepoints in the middle of each side of the ball
# makes it much easier to determine the direction ball should bounce

import sys, pygame
pygame.init()
# set up the clock
clock = pygame.time.Clock()

# set colors
black = 0, 0, 0

# set screen variables
width, height = 1000, 1000
size = width, height
# create the 'screen' surface
screen = pygame.display.set_mode(size)

# load ball image 
ball = pygame.image.load("intro_ball.gif")
# frame surface of the rectanglular dimensions of the ball surface
ballrect = ball.get_rect()

# setup a list for ball x and y speeds
speed = [10, 10]

# create the bumper surface and rect from the sammich
bumper = pygame.image.load("halt_hand.png")
bumperrect = bumper.get_rect()

# set location of bumper at center of screen - our bumper isn't moving
bumpX = 420
bumpY = 350

# while loop control
go = True
while go:
    # event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False # graceful exit() from the sys library
    # the rect object is key in pygame
    # .move() takes 2 inputs for x and y
    ballrect = ballrect.move(speed)
    # put bumper on screen
    bumperrect.x = bumpX
    bumperrect.y = bumpY
    # code to keep ball on the screen
    if ballrect.left < 0 or ballrect.right > width: # uses edges of ballrect surface to detect collision with screen surface
        speed[0] = -speed[0] # reverse horizontal speed to stay on screen
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1] # reverse vertical speed to stay on screen
    # conditions to get ball to bounce off sammich properly
    # these numbers are carefully calculated to screen size, image size and image location
    # i use a "fudge" factor of speed[0] or [1] to make certain the collisions work
    # setup ball collide points at midpoints of each ball rect line
    balltop = (ballrect.x + 50, ballrect.top)
    ballleft = (ballrect.left, ballrect.y + 50)
    ballright = (ballrect.right, ballrect.y + 50)
    ballbottom = (ballrect.x + 50, ballrect.bottom)
    # check collision
    if bumperrect.collidepoint(ballleft):
        speed[0] = -speed[0]
    if bumperrect.collidepoint(balltop):
        speed[1] = -speed[1]
    if bumperrect.collidepoint(ballright):
        speed[0] = -speed[0]
    if bumperrect.collidepoint(ballbottom):            
        speed[1] = -speed[1]

    screen.fill(black) # note we refill the screen w/ black every flip() so no ghost trails :)
    # add the sammich bumper to the screen
    screen.blit(bumper, bumperrect)
    screen.blit(ball, ballrect) # screen.blit takes 2 params - the first, ball, is drawn onto the second, ballrect surface
    pygame.display.flip()
    clock.tick(60) # run the clock as 60 FPS
pygame.quit()