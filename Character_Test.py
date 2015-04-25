#Pygame Template
#IndustrialPopsicle

import pygame
import time
import math
import random
import pyganim

#Here are some colors.
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
yellow   = ( 255, 255,   0)
BGCOLOR = (100, 50, 50)
pygame.init()
size = [1200,800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")


###########################################################################
## Variables
speed=.045

animate=False

x_coord=560
y_coord=340

run_speed=5

move_up=False
move_down=False
move_right=False
move_left=False
sprint=False


###############

##  Lists



###############

## Fonts




###############

## Images
stand_up=pygame.image.load("Data/standing/up.png")
stand_down=pygame.image.load("Data/standing/down.png")
stand_left=pygame.image.load("Data/standing/left.png")
stand_right=pygame.image.load("Data/standing/right.png")


###############

## Animations
run_up=pyganim.PygAnimation([('Data/Up/up_1.png', speed),
                             ('Data/Up/up_2.png', speed),
                             ('Data/Up/up_3.png', speed),
                             ('Data/Up/up_4.png', speed),
                             ('Data/Up/up_5.png', speed),
                             ('Data/Up/up_6.png', speed),
                             ('Data/Up/up_7.png', speed),
                             ('Data/Up/up_8.png', speed),
                             ('Data/Up/up_9.png', speed)])
run_down=pyganim.PygAnimation([('Data/down/down_1.png', speed),
                             ('Data/down/down_2.png', speed),
                             ('Data/down/down_3.png', speed),
                             ('Data/down/down_4.png', speed),
                             ('Data/down/down_5.png', speed),
                             ('Data/down/down_6.png', speed),
                             ('Data/down/down_7.png', speed),
                             ('Data/down/down_8.png', speed),
                             ('Data/down/down_9.png', speed)])
run_left=pyganim.PygAnimation([('Data/left/left_1.png', speed),
                             ('Data/left/left_2.png', speed),
                             ('Data/left/left_3.png', speed),
                             ('Data/left/left_4.png', speed),
                             ('Data/left/left_5.png', speed),
                             ('Data/left/left_6.png', speed),
                             ('Data/left/left_7.png', speed),
                             ('Data/left/left_8.png', speed),
                             ('Data/left/left_9.png', speed)])
run_right=pyganim.PygAnimation([('Data/right/right_1.png', speed),
                             ('Data/right/right_2.png', speed),
                             ('Data/right/right_3.png', speed),
                             ('Data/right/right_4.png', speed),
                             ('Data/right/right_5.png', speed),
                             ('Data/right/right_6.png', speed),
                             ('Data/right/right_7.png', speed),
                             ('Data/right/right_8.png', speed),
                             ('Data/right/right_9.png', speed)])
selected_animation=run_down

###############

## Functions



###############

## Classes



###############

## objects



###############
###########################################################################
run_down.play()
run_down.pause()


done = False
mainClock = pygame.time.Clock()

# -------- Main Program Loop ----------- #
move_up=False
move_down=False
move_left=False
move_right=False
while done == False:
    ## Events
    screen.fill(BGCOLOR)
    movement="none"

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_up=False
                    move_down=False
                    move_left=False
                    move_right=False
                    run_up.play()
                    
                    selected_animation=run_up
                    move_up=True

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    run_up.pause()
                    
                    move_up=False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    move_up=False
                    move_down=False
                    move_left=False
                    move_right=False
                    run_down.play()
                    
                    selected_animation=run_down
                    move_down=True

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    run_down.pause()
                    
                    move_down=False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_up=False
                    move_down=False
                    move_left=False
                    move_right=False
                    run_left.play()
                    move_left=True
                    
                    selected_animation=run_left
                    

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    run_left.pause()
                    
                    move_left=False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    move_up=False
                    move_down=False
                    move_left=False
                    move_right=False
                    run_right.play()
                    
                    selected_animation=run_right
                    move_right=True

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    run_right.pause()
                    
                    move_right=False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    run_speed*=2

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    run_speed/=2
                    




    ###############
      
    ## Logic
    



    if move_up==True:
        y_coord=y_coord-run_speed
    if move_down==True:
        y_coord=y_coord+run_speed
    if move_left==True:
        x_coord=x_coord-run_speed
    if move_right==True:
        x_coord=x_coord+run_speed
        
    
     


    ##   Draw
    selected_animation.blit(screen, (x_coord,y_coord))

     
    ###############
    
    pygame.display.flip()    
    mainClock.tick(60)   #FPS  

