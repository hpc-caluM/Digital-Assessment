
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

#Walking animation
character_surface = pygame.image.load('assets/Character1M_3_walk_1.png').convert_alpha()       
character_rect = character_surface.get_rect(center = (500,500))

character_surface = [pygame.image.load("assets/Character1M_3_walk_1.png"),
                pygame.image.load("assets/Character1M_3_walk_2.png"),
                pygame.image.load("assets/Character1M_3_walk_3.png"),
                pygame.image.load("assets/Character1M_3_walk_4.png"),
                pygame.image.load("assets/Character1M_3_walk_5.png"),
                pygame.image.load("assets/Character1M_3_walk_6.png"),
                pygame.image.load("assets/Character1M_3_walk_7.png")]
clock = pygame.time.Clock()
ANIMATION = pygame.USEREVENT
pygame.time.set_timer(ANIMATION, 150)
run = True
moving = False
image_index = 0
velocity = 12
x = 500
y = 500

#idle animation
character_idle = [pygame.image.load("assets/Character1M_3_idle_0.png"),
                pygame.image.load("assets/Character1M_3_idle_1.png"),
                pygame.image.load("assets/Character1M_3_idle_2.png"),
                pygame.image.load("assets/Character1M_3_idle_3.png"),
                pygame.image.load("assets/Character1M_3_idle_4.png"),
                pygame.image.load("assets/Character1M_3_idle_5.png"),
                pygame.image.load("assets/Character1M_3_idle_6.png"),
                pygame.image.load("assets/Character1M_3_idle_7.png")]
ANIMATION = pygame.USEREVENT
pygame.time.set_timer(ANIMATION, 150)
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
                image_index = 0
        
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_w or event.key == pygame.K_s:
                moving = False  
                image_index = 0
                
        if event.type == ANIMATION:
          
            if image_index < len(character_surface)-1: 
                image_index += 1
            else:
                image_index = 0
                    
   #Walking animation
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]: 
            character_rect.x -= 1
            moving = True
    if keys[pygame.K_d]: 
            character_rect.x += 1
            moving = True
            
    if keys[pygame.K_w]:
            character_rect.y -= 1
            moving = True
    if keys[pygame.K_s]:
            character_rect.y += 1
            moving = True
            
            character_movement = 0
            character_movement -= 0
            
    if moving:
        current_sprite = character_surface[image_index]
    else:
        current_sprite = character_idle[image_index] 
    
    SCREEN.blit(bg_surface, (0,0))
    
    SCREEN.blit(current_sprite, character_rect)
    print(character_rect.x, character_rect.y)
    #pygame.draw.rect(SCREEN,pygame.Color("white"),character_rect)
    
    #window.blit(current_sprite, (x, y))

    
    pygame.display.update()
    clock.tick(60)