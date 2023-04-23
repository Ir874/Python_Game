# Imports
import pygame 
import sys
from pygame.locals import *
from time import sleep
import random

# Pygame initialization
pygame.init()

# Window startup code
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
 
# Game loop
while True:
  screen.fill((0, 0, 0)) # Setting screen color
  
  # Event capture loop
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN: # Detecting Key input
      
      if event.key == pygame.K_d: # Detecting D key
        print("D")
      
      if event.key == pygame.K_s: # Detecting S key
        print("S")

      if event.key == pygame.K_a: # Detecting A key
        print("A")
      
      if event.key == pygame.K_f: # Detecting J key
        print("F")

    

# Frame updater
pygame.display.flip()

