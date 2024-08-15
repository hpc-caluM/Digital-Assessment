from urllib.parse import scheme_chars
import pygame, sys

from pygame.locals import QUIT
pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1920, 1020
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Creeping Silence')

#Game variables (images/sprites)
character_movement = 0
bg_surface = pygame.image.load('assets/Assessment Map.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))

character_surface = pygame.image.load('assets/Character1M_3_walk_1.png').convert_alpha()       
character_rect = character_surface.get_rect(center = (500,500))

character_surface = pygame.image.load('assets/Character1M_3_walk_2.png').convert_alpha()       
character_rect = character_surface.get_rect(center = (500,500))

character_surface = pygame.image.load('assets/Character1M_3_walk_3.png').convert_alpha()       
character_rect = character_surface.get_rect(center = (500,500))
    


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

   
    
#The player code
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_a]: 
            character_rect.x -= 1
    if keys[pygame.K_d]: 
            character_rect.x += 1
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
            character_rect.y -= 1
    if keys[pygame.K_s]:
            character_rect.y += 1
            
            character_movement = 0
            character_movement -= 0
    
    SCREEN.blit(bg_surface, (0,0))
    
    SCREEN.blit(character_surface, character_rect)
    #pygame.draw.rect(SCREEN,pygame.Color("white"),character_rect)

    
    pygame.display.update()
    clock.tick(60)