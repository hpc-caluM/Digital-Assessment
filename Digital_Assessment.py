import pygame, sys

from pygame.locals import QUIT
pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Creeping Silence')


bg_surface = pygame.image.load('assets/Assessment Map.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            

    SCREEN.blit(bg_surface, (0,0))
    
    pygame.display.update()