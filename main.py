import pygame
import os
import time

from PIL import Image #Needed to get dimensions of map assets

pygame.init()

resolution_X = 600
resolution_Y = 900

screen = pygame.display.set_mode((resolution_X,resolution_Y))

pygame.display.set_caption("Wavekicker 3000")

clock = pygame.time.Clock()
clock.tick(24)

# Create player and initial position
player = pygame.image.load("./ert/player.png")
playerX = 300
playerY = 700
# Movement for player
deltaX = 0
deltaY = 0

kick = pygame.image.load("./ert/player.png")

def draw_player(x,y):
    screen.blit(player, (x,y)) #Draw player at specific inputs

def kick_wave(x,y):
    screen.blit(kick, (x,y-100)) #Draw kick

    
#edit this so that water moves when certain conditions are met
background_timer = 0
background_file = "./ert/background_extend.png"
background = pygame.image.load(background_file)

def draw_background(n):     #   Check to see if it exists
    global background, backfround_file
    if os.path.isfile(background_file) and n < 300:
        screen.blit(background, [0, n-300]) #y=-300 starting position
    else:
        screen.blit(background, [0, 0]) #stops moving the picture. Game Over

#   How to handle dynamic movement
# Want it slower when in water
#maybe only update every few frames?
def player_speed(playerX, playerY):
    #global background_timer                 #gota subtract background timer to properly update surf color
    surf_color = background.get_at((playerX, abs(playerY-int(background_timer))))[0]  #gets the R color at the player's position    
    
    if surf_color > 43:
        speed = 6
    elif surf_color <= 43 and surf_color >= 10:
        speed = 3
    else:
        speed = 2
    print(speed, surf_color, playerY)
    return speed

def flashing_message(message):
    font = pygame.font.Font("./fonts/Karate.ttf", 32)
    message_display = font.render(message, True, (255, 255, 255))
    screen.blit(message_display, (200, 200))

# --------------------------------------------------------------------------------------------
#
#                               The Primary Gameplay Loop
#
# --------------------------------------------------------------------------------------------
game_running = True

while game_running:
    for event in pygame.event.get():  # Captures all of the events in pygame.
        if event.type == pygame.QUIT:  # If the event type is 'qutting the game', AKA the 'close' button
            game_running = False  # Only stops when close button is pressed

    #   -------------------------
    #       Player Movement
    #   -------------------------
    if event.type == pygame.KEYDOWN:  # KEYDOWN = when tehkey is pressed
        if event.key == pygame.K_LEFT:  # K_LEFT = left arrow key
            deltaX = -player_speed(playerX, playerY)  # Increment player left

        if event.key == pygame.K_RIGHT:  # K_RIGHT = right arrow key
            deltaX = player_speed(playerX, playerY)  # Increment player right

        if event.key == pygame.K_UP:  # K_UP = up arrow key
            deltaY = -player_speed(playerX, playerY)  # Increment player up

        if event.key == pygame.K_DOWN:  # K_DOWN = down arrow key
            deltaY = player_speed(playerX, playerY)  # Increment player down

        if event.key == pygame.K_SPACE:  # K_DOWN = down arrow key
            kick_wave(playerX, playerY)


    # If keys are released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            deltaX = 0  # When key is not pressed, we stop movement
            deltaY = 0  # Stop movement when key si released

    # Update player's position
    playerY += deltaY
    playerX += deltaX

    

    #   Player Movement - Out of Frame
    if playerY < 10:
        playerY = 10
    elif playerY >= 850:
        playerY = 850
    if playerX < 0:
        playerX = 0
    elif playerX >= 575:
        playerX = 575

    draw_background(background_timer)
    background_timer += 0.1           #Change this to be a certain criteria, ie missed waves
    if background_timer >= 300:     #If beach is entirely gone, Game OVer
        flashing_message("GAME OVER")

    draw_player(playerX, playerY)
    #flashing_message("Tides Coming In!!!")

    pygame.display.update()
