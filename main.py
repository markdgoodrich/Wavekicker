import pygame
import os
import time

from PIL import Image #Needed to get dimensions of map assets

pygame.init()

resolution_X = 600
resolution_Y = 900

screen = pygame.display.set_mode((resolution_X,resolution_Y))

pygame.display.set_caption("Wavekicker 3000")


# Create player and initial position
player = pygame.image.load("./ert/player.png")
playerX = 300
playerY = 700
# Movement for player
deltaX = 0
deltaY = 0

def draw_player(x,y):
    screen.blit(player, (x,y)) #Draw player at specific inputs

def draw_background():
    background_file = "./ert/background.png"
     #   Check to see if it exists
    if os.path.isfile(background_file):
        screen.blit(pygame.image.load(background_file), [0, 0])


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
            deltaX = -6  # Increment player left by 5 values

        if event.key == pygame.K_RIGHT:  # K_RIGHT = right arrow key
            deltaX = 6  # Increment player left by 5 values

        if event.key == pygame.K_UP:  # K_LEFT = left arrow key
            deltaY = -6  # Increment player left by 5 values

        if event.key == pygame.K_DOWN:  # K_RIGHT = right arrow key
            deltaY = 6  # Increment player left by 5  values

    # If keys are released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            deltaX = 0  # When key is not pressed, we stop movement
            deltaY = 0  # Stop movement when key si released

    # Update player's position
    playerY += deltaY
    playerX += deltaX

    
    draw_background()

    draw_player(playerX, playerY)


    pygame.display.update()
