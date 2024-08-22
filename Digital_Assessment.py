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
bg_surface = pygame.transform.scale(bg_surface,(WIDTH, HEIGHT))

character_surface = pygame.image.load('assets/Character1M_3_walk_1.png').convert_alpha()       
character_rect = character_surface.get_rect(center = (500,500))

character_surface = [pygame.image.load("assets/Character1M_3_walk_1.png"),
                pygame.image.load("assets/Character1M_3_walk_2.png"),
                pygame.image.load("assets/Character1M_3_walk_3.png"),
                pygame.image.load("assets/Character1M_3_walk_4.png"),
                pygame.image.load("assets/Character1M_3_walk_5.png"),
                pygame.image.load("assets/Character1M_3_walk_6.png"),
                pygame.image.load("assets/Character1M_3_walk_7.png"),]
clock = pygame.time.Clock()
ANIMATION = pygame.USEREVENT
pygame.time.set_timer(ANIMATION, 500, 500)
run = True
moving = False
image_index = 0
velocity = 12
x = 500
y = 500

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

   
    
#The player code

        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_a or event.key == pygame.K_d:
                moving = False  
                image_index = image_index
        
                if event.type == ANIMATION:
                    if moving:
                        if image_index < len(image_sprite)-1: 
                            image_index += 1
                        else:
                            image_index = 0
                    
    #window.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

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
            
    current_sprite = character_surface[image_index]
    
    SCREEN.blit(bg_surface, (0,0))
    
    SCREEN.blit(character_surface[0],character_rect)
    #pygame.draw.rect(SCREEN,pygame.Color("white"),character_rect)
    
    #window.blit(current_sprite, (x, y))

    
    pygame.display.update()
    clock.tick(60)