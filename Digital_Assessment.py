
import pygame, sys

from pygame.locals import QUIT
pygame.init()
clock = pygame.time.Clock()

#The Screen and Title
WIDTH, HEIGHT = 900, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lost')

#Game variables (images/sprites)
character_movement = 0
bg_surface = pygame.image.load('assets/Assessment Map.png').convert()
bg_surface = pygame.transform.scale(bg_surface,(WIDTH, HEIGHT))

#Walking animation
character_surface = pygame.image.load('assets/Character1M_3_walk_1.png').convert_alpha()       
character_rect = character_surface.get_rect(center = (670,325))

character_surface = [pygame.image.load("assets/Character1M_3_walk_1.png"),
                pygame.image.load("assets/Character1M_3_walk_2.png"),
                pygame.image.load("assets/Character1M_3_walk_3.png"),
                pygame.image.load("assets/Character1M_3_walk_4.png"),
                pygame.image.load("assets/Character1M_3_walk_5.png"),
                pygame.image.load("assets/Character1M_3_walk_6.png"),
                pygame.image.load("assets/Character1M_3_walk_7.png")]

character_flip = []

for i in range(len(character_surface)):
     character_flip.append(pygame.transform.flip(character_surface[i], True, False))


character_rect = pygame.Rect(100,100,20,30)
 
# = [pygame.Rect(200,350,50,50),pygame.Rect(260,320,50,50)]

#Objects (where i code the map pieces for progression)

key1_rect = pygame.Rect(611,59,20,20)
#key2_rect = pygame.Rect()
#key3_rect = pygame.Rect()
#key4_rect = pygame.Rect()
#key5_rect = pygame.Rect()

key_list = [key1_rect]

#Object sprites    
key1_rect = [pygame.image.load("assets/BD3  (7).png")]
#key2_rect = [pygame.image.load("assets/pygame.image.load(BD3(7).png")]
#key3_rect = [pygame.image.load("assets/pygame.image.load(BD3(7).png")]           
#key4_rect = [pygame.image.load("assets/pygame.image.load(BD3(7).png")]   
#key5_rect = [pygame.image.load("assets/pygame.image.load(BD3(7).png")]   



#Extra Collision code
def collision_test(character_rect,wall_list):
    collisions = []
    for wall in wall_list:
        if character_rect.colliderect(wall):
            collisions.append(wall)
    return collisions
 
def move(character_rect,movement,wall_list): # movement = [5,2]
    character_rect.x += movement[0]
    collisions = collision_test(character_rect,wall_list)
    for wall in collisions:
        if movement[0] > 0:
            character_rect.right = wall.left
        if movement[0] < 0:
            character_rect.left = wall.right
    character_rect.y += movement[1]
    collisions = collision_test(character_rect,wall_list)
    for wall in collisions:
        if movement[1] > 0:
            character_rect.bottom = wall.top
        if movement[1] < 0:
            character_rect.top = wall.bottom
    return character_rect

right = False
left = False
up = False
down = False


clock = pygame.time.Clock()
run = True
moving = False
facingleft = False
image_index = 0
velocity = 12
x = 500
y = 500

collision = False

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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos()) 

    #pygame.transform.flip(character_surface)
    

    #The character_rect code


        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_a or event.key == pygame.K_d:
                moving = False  
                image_index = 0
        
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_w or event.key == pygame.K_s:
                moving = False  
                image_index = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_w:
                up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_s:
                down = False
            if event.key == pygame.K_w:
                up = False
                
        if event.type == ANIMATION:
          
            if image_index < len(character_surface)-1: 
                image_index += 1
            else:
                image_index = 0 
                
   #Walking animation
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]: 
            #character_rect.x -= 1
            moving = True
            facingleft = True
            #left = True
    if keys[pygame.K_d]: 
            #character_rect.x += 1
            moving = True
            facingleft = False
            #right = True
            
    if keys[pygame.K_w]:
            #character_rect.y -= 1
            moving = True
            #up = True
    if keys[pygame.K_s]:
            #character_rect.y += 1
            moving = True
            #down = True
            
    #character_movement = 0
    #character_movement -= 0
    
    #Collisions (The boxes that i draw so i know where to do the collisions)
    wall1 = pygame.Rect(54, 235, 635, 270)
    
    wall_list = [wall1]
    
    #rect collision (the actual colliding factor)
    
    for wall in wall_list:
            if character_rect.colliderect (wall):
                collision = True
                print (collision)
                
            if character_rect.right >= WIDTH or character_rect.left <= 0:
                character_rect.x *= -1
    if character_rect.right >= WIDTH or character_rect.top <= 0:
        character_rect.y *= -1
    if character_rect.right >= WIDTH or character_rect.bottom <= 0:
        character_rect.y *= -1
    if character_rect.bottom >= HEIGHT:
        character_rect.y *= -1
    
    
    #clear display
        SCREEN.fill((0,0,0))
 
    movement = [0,0]
    if right == True:
        movement[0] += 2
    if left == True:
        movement[0] -= 2
    if up == True:
        movement[1] -= 2
    if down == True:
        movement[1] += 2
        
    keys = pygame.key.get_pressed()
    



 
    character_rect = move(character_rect,movement,wall_list)
 
    pygame.draw.rect(SCREEN,(255,255,255),character_rect)
 
    for wall in wall_list:
        pygame.draw.rect(SCREEN,(255,0,0),wall)
             
   
    
            
    if moving:
        if facingleft:
            current_sprite = character_flip[image_index] 
        else:
             
            current_sprite = character_surface[image_index]
    else:
        current_sprite = character_idle[image_index] 
    
    SCREEN.blit(bg_surface, (0,0))
    
    SCREEN.blit(current_sprite, character_rect)
    #print(character_rect.x, character_rect.y)
    
    #pygame.draw.rect(SCREEN, pygame.Color('red'), wall1)
    #pygame.draw.rect(SCREEN,pygame.Color("white"),character_rect)
    
    #window.blit(current_sprite, (x, y))

    #Object number 1 drawn
    for key in key_list:
        #pygame.draw.rect(SCREEN,pygame.Color("pink"),key)
      
        
        pygame.display.update()
    clock.tick(60)