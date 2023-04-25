# Imports
import pygame 
import sys
from pygame.locals import *
from time import sleep
import random

# Pygame initialization
pygame.init()

# Initialize FPS clock
clock = pygame.time.Clock()

# Window startup code
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

# Defining the FASD buttons 
F = pygame.Surface((20, 20))
A = pygame.Surface((20, 20))
S = pygame.Surface((20, 20))
D = pygame.Surface((20, 20)) 




# Game loop
while True:
  screen.fill((255, 255, 255)) # Setting screen color
  
  # Put the FASD buttons onto the screen
  screen.blit(D,(220,100))
  screen.blit(A,(100,100))
  screen.blit(S,(140,100))
  screen.blit(F,(180,100))

  # Event capture loop
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN: # Detecting Key input
      
      if event.key == pygame.K_d: # Detecting D key
        D.fill((255,255,0))
        sleep(0.5)
        D.fill((0,0,0))

      if event.key == pygame.K_s: # Detecting S key
        S.fill((0,0,255))
        sleep(0.5)
        S.fill((0,0,0))

      if event.key == pygame.K_a: # Detecting A key
        A.fill((0,255,0))
        sleep(0.5)
        A.fill((0,0,0))

      if event.key == pygame.K_f: # Detecting F key
        F.fill((255,0,0))
        sleep(0.5)
        F.fill((0,0,0))

    
    # Frame updater
    pygame.display.update()

    # Fps setter
    clock.tick(60)
    


