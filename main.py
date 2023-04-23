# Imports
import pygame 
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
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()

# Frame updater
pygame.display.flip()

