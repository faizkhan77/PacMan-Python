import pygame
from board import boards
import math

pygame.init() # initializing pygame

# width and height of our screen
WIDTH = 635
HEIGHT = 700

screen = pygame.display.set_mode([WIDTH, HEIGHT])    # Setting the pygame screen using HEIGHT AND WIDTH variable

"""STATIC VARIABLES"""
timer = pygame.time.Clock() # to control the speed your game runs
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)  # Setting game font style and size
level = boards
color = 'red'  #setting tiles color
PI = math.pi    # we need PI to be able to draw arcs, the corners tiles

# Getting player images using for loop
player_images = []
for i in range(1, 5):   #Taking all the pac images and scaling it to 35,35 and appending it to player_images var
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (33, 33)))
    
#initial position of pac
player_x = 300
player_y = 473
direction = 0
counter = 0
flicker = False

def draw_boards():
    num1 = ((HEIGHT - 50) // 32)    # define how wide n how tall each tiles should be, height - 50 then devide by 32 since theres 32 vertical items in pacman
    num2 = (WIDTH // 30)    # how wide the board is devide by 50
    for i in range(len(level)): # for every row iterate through
        for j in range(len(level[i])):  # iterate through for every column inside that specific row
            if level[i][j] == 1: # if its small dots draw it on screen with white color and poditioning then 4 is size
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2 and not flicker: # if its big dots draw it on screen with white color and poditioning then 10 is size
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3: # drawing the 3rd line on screen, setting color, and giving x and y coordinates, then thickness
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 2) # 3 is thickness of the line
            if level[i][j] == 4: 
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1) ),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 2)
                
            if level[i][j] == 5: 
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.4))-2, (i * num1 + (0.5*num1)), num2, num1], 0, PI/2, 2)
                
            if level[i][j] == 6: 
                pygame.draw.arc(screen, color, [(j*num2 + (num2*0.5)), (i * num1 + (0.5*num1)), num2, num1], PI/2, PI, 2)
                
            if level[i][j] == 7: 
                pygame.draw.arc(screen, color, [(j*num2 + (num2*0.5)), (i * num1 - (0.4*num1)), num2, num1], PI, 3*PI/2, 2)
                
            if level[i][j] == 8: 
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.4))-2, (i * num1 - (0.4*num1)), num2, num1], 3*PI / 2, 2*PI, 2)
                
            if level[i][j] == 9: # tiles 4 and 9 is the same since they are horizontal, only diff is color, TILE 9 IS DOOR OF GHOST
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1) ),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 2)


def draw_player():
    if direction == 0: # pac will have 4 diff directions, counter is to track how fast pac should move, counter devide by 5, 0 IS RIGHT DIRECTION
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1: # LEFT DIRECTION
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2: # UP DIRECTION
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3: # DOWN DIRECTION 
        screen.blit(pygame.transform.rotate(player_images[counter // 5], -90), (player_x, player_y))


# Setting run variable and while loop to keep the game running
run = True
while run:
    timer.tick(fps) # controlling speed according to the fps variable
    
    if counter < 19:
        counter += 1
        if counter > 3:    # Speed of flickering of big balls, more means faster, low num means slower flicker
            flicker = False
    else:
        counter = 0
        flicker = True
    
    screen.fill('black')    # Putting a black color in the background
    
    draw_boards()
    draw_player()
    
    # To get all the events happening in the screen (e.g. input,keyboard, mouse, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # If event type is quit means the red X button then make run False
            run = False
        # ESCAPE button to quit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            
        # Pac direction control with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3
    
    pygame.display.flip()   # to make everything on the screen every iteration
    
pygame.quit()