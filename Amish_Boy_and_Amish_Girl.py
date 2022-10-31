# CSCN 345 (003) Python Game by Isaac Scott and Ryan Bender

import sys
import pygame
import spritesheet
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 600
WIDTH = 1250
ACC = 0.5
FRIC = -0.12
FPS = 120

P1com = False
P2com = False
bg = pygame.image.load('bgimgFade.png') # Loads background image into bg variable
totalcomplete = 0

wina = pygame.image.load('wina.png') # Loads boy win screen
winb = pygame.image.load('winb.png') # loads girl win screen
lose = pygame.image.load('gameover.png') # Loads losing screen
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amish Boy and Amish Girl")

# Loads sprite sheet image into variable 
boy_sprite_sheet_image = pygame.image.load('boy_sprite_sheet.png').convert_alpha()
girl_sprite_sheet_image = pygame.image.load('Girl Sprite Sheet.png').convert_alpha()

# Black color key
BLACK = (0, 0, 0)

# Initializes a spritesheet class for each player
boy_sprite_sheet = spritesheet.SpriteSheet(boy_sprite_sheet_image)
girl_sprite_sheet = spritesheet.SpriteSheet(girl_sprite_sheet_image)

# Clock
def clock():
    currentTime = pygame.time.get_ticks()
    return currentTime

#class for player
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.pos = vec((WIDTH - 100, HEIGHT - 11))
        self.vel = vec(0,0)

        # sprites
        self.sprites = []
        bframe0 = self.sprites.append(spritesheet.getImageBoy(boy_sprite_sheet_image, 0, 49, 67, BLACK, 1))
        bframe1 = self.sprites.append(spritesheet.getImageBoy(boy_sprite_sheet_image, 1, 49, 67, BLACK, 1))
        bframe2 = self.sprites.append(spritesheet.getImageBoy(boy_sprite_sheet_image, 2, 49, 67, BLACK, 1))
        bframe3 = self.sprites.append(spritesheet.getImageBoy(boy_sprite_sheet_image, 3, 49, 67, BLACK, 1))
        bframe4 = self.sprites.append(spritesheet.getImageBoy(boy_sprite_sheet_image, 4, 49, 67, BLACK, 1))
        bframe5 = self.sprites.append(spritesheet.getImageBoy(boy_sprite_sheet_image, 5, 49, 67, BLACK, 1))
        
        self.current_sprite = 0
        self.surf = self.sprites[self.current_sprite]
        self.rect = self.surf.get_rect()
    
    #colision update
    def update1(self):

        hitsf = pygame.sprite.spritecollide(P1 ,platforms, False)
        hitsw = pygame.sprite.spritecollide(P1 ,walls, False)
        if P1.vel.x > 0:        
            if hitsw:
                self.vel.x = 0
                self.pos.x = hitsw[0].rect.left - 25
        if P1.vel.x < 0:        
            if hitsw:
                self.vel.x = 0
                self.pos.x = hitsw[0].rect.right + 25
      
            
        if P1.vel.y > 0:        
            if hitsf:
                self.vel.y = 0
                self.pos.y = hitsf[0].rect.top + 1
        if P1.vel.y < 0:        
            if hitsf:
                self.vel.y = 15       
                
    #movement function
    def move1(self):

        it = False

        self.acc = vec(0,0.5)
 
        pressed_keys = pygame.key.get_pressed()
            
        nextFrame = clock()
        frame = 0
        while True:
            if clock() > nextFrame:
                frame = (frame+1) % 8
                nextFrame += 80

            if pressed_keys[K_RIGHT]:
                spritesheet.changeSpriteImage(boy_sprite_sheet_image, 0*3+frame)
            elif pressed_keys[K_LEFT]:
                spritesheet.changeSpriteImage(boy_sprite_sheet_image, 1*3+frame)


        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            # # self.current_sprite = self.current_sprite + 1
            # # if self.current_sprite >= len(self.sprites) - 3:
            # #   self.current_sprite = self.current_sprite -1
            # # elif self.current_sprite <= len(self.sprites) - 5:
            # #     self.current_sprite = self.current_sprite + 1
            # # else:
            # #   self.current_sprite = 0

            # # self.surf = self.sprites[self.current_sprite]
            # # self.rect = self.surf.get_rect()

            #   it = True
            # elif it == True:  
            #     self.current_sprite = 0
            #     it = False
            #     self.surf = self.sprites[self.current_sprite]
            #     self.rect = self.surf.get_rect()
            # else:
            #     self.current_sprite = 0


        if pressed_keys[K_RIGHT]:        
            self.acc.x = ACC
            # # self.current_sprite = self.current_sprite + 1
            # # if self.current_sprite >= len(self.sprites):
            # #   self.current_sprite = self.current_sprite - 1
            # # elif self.current_sprite <= len(self.sprites) - 2:
            # #     self.current_sprite = self.current_sprite + 1
            # # else: 
            # #   self.current_sprite = 3

            # # self.surf = self.sprites[self.current_sprite]
            # # self.rect = self.surf.get_rect()
            
            #   it = True
            # elif it == True:  
            #     self.current_sprite = 3
            #     it = False
            # else:
            #     self.current_sprite = 3

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos
        
 #jump function
    def jump1(self):
 
        hits1 = pygame.sprite.spritecollide(self, platforms, False)
        if hits1:
            self.vel.y = -15
            
class Player2(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.pos = vec((100, HEIGHT - 11))
        self.vel = vec(0,0)
    
        # sprites
        self.sprites = []
        self.sprites.append(spritesheet.getImageGirl(girl_sprite_sheet_image, 0, 41, 69, BLACK, 1))
        self.sprites.append(spritesheet.getImageGirl(girl_sprite_sheet_image, 1, 41, 69, BLACK, 1))
        self.sprites.append(spritesheet.getImageGirl(girl_sprite_sheet_image, 2, 41, 69, BLACK, 1))
        self.sprites.append(spritesheet.getImageGirl(girl_sprite_sheet_image, 3, 41, 69, BLACK, 1))
        self.sprites.append(spritesheet.getImageGirl(girl_sprite_sheet_image, 4, 41, 69, BLACK, 1))
        self.sprites.append(spritesheet.getImageGirl(girl_sprite_sheet_image, 5, 41, 69, BLACK, 1))

        self.current_sprite = 3
        self.surf = self.sprites[self.current_sprite]
        self.rect = self.surf.get_rect()
    
        
    #colision update   
    def update2(self):

        hitsf = pygame.sprite.spritecollide(P2 ,platforms, False)
        hitsw = pygame.sprite.spritecollide(P2 ,walls, False)
        if P2.vel.x > 0:        
            if hitsw:
                self.vel.x = 0
                self.pos.x = hitsw[0].rect.left - 25
        if P2.vel.x < 0:        
            if hitsw:
                self.vel.x = 0
                self.pos.x = hitsw[0].rect.right + 25
        if P2.vel.y > 0:        
            if hitsf:
                self.vel.y = 0
                self.pos.y = hitsf[0].rect.top + 1
        if P2.vel.y < 0:        
            if hitsf:
                self.vel.y = 15   
            
    #movement function        
    def move2(self):
        self.acc = vec(0,0.5)
 
        pressed_keys = pygame.key.get_pressed()    
        
        if pressed_keys[K_a]:
            self.acc.x = -ACC

        if pressed_keys[K_d]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos          
        
 #jump function    
    def jump2(self):
       
        hits2 = pygame.sprite.spritecollide(self, platforms, False)
        if hits2:
            self.vel.y = -15
#walls
class wall(pygame.sprite.Sprite):
    def __init__(self, sizex, sizey, posx, posy):
        super().__init__()
        if sizey < 30:
            self.surf = pygame.Surface((sizex + 4, 0))
        else:
            self.surf = pygame.Surface((sizex + 4, sizey - 21))
        self.surf.fill((150,100,0))
        self.rect = self.surf.get_rect(center = (posx, posy))
        
#class for platforms 
class platform(pygame.sprite.Sprite):
    def __init__(self, sizex, sizey, posx, posy):
        super().__init__()
        self.surf = pygame.Surface((sizex, sizey))
        self.surf.fill((150,100,0))
        self.rect = self.surf.get_rect(center = (posx, posy))

        
class goal(pygame.sprite.Sprite):
     def __init__(self):
         super().__init__()
         self.surf = pygame.Surface((20, 20))
         self.surf.fill((255,255,12))
         self.rect = self.surf.get_rect(center = (100, 50))
 
class go(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = lose
        self.rect = self.surf.get_rect()
        
class wa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = wina
        self.rect = self.surf.get_rect()
        
class wb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = winb
        self.rect = self.surf.get_rect()
        
def gameover():
    g = go()
    all_sprites.add(g)  
    
def wina():
    won = wa()
    all_sprites.add(won)
    
def winb():
    won = wb()
    all_sprites.add(won)    
        
#player colision detection        
def colision(boy, com1, com2):
    players2 = pygame.sprite.Group()
    players2.add(P2)
    hitsgo = pygame.sprite.spritecollide(boy, players2, False)
    if hitsgo:
        gameover()
    players1 = pygame.sprite.Group()
    players1.add(P1)
    #Win statment
    #amish boy win
    hitsw1 = pygame.sprite.spritecollide(obj, players1, False)
    if hitsw1:
        wina()
      
      #amish girl win  
    hitsw2 = pygame.sprite.spritecollide(obj, players2, False)
    if hitsw2:
        winb()
    
    
        
    
    

        
        
PT1 = platform(WIDTH, 20, WIDTH/2, HEIGHT-10)
WALL1 = wall(WIDTH, 20, WIDTH/2, HEIGHT-10)
PT2 = platform(50, 50, WIDTH/2, HEIGHT-20)
WALL2 = wall(50, 50, WIDTH/2, HEIGHT-20)
PT3 = platform(20, HEIGHT /2, 10, HEIGHT/4*3)
WALL3 = wall(20, HEIGHT/2, 10, HEIGHT/4*3)
PT4 = platform(20, HEIGHT /2, WIDTH - 10, HEIGHT/4*3)
WALL4 = wall(20, HEIGHT/2, WIDTH - 10, HEIGHT/4*3)
PT5 = platform(20, HEIGHT /2, 200, HEIGHT/4*3)
WALL5 = wall(20, HEIGHT/2, 200, HEIGHT/4*3)
PT6 = platform(20, HEIGHT /2, WIDTH - 200, HEIGHT/4*3)
WALL6 = wall(20, HEIGHT/2, WIDTH - 200, HEIGHT/4*3)
PT7 = platform(50, 50, 35, HEIGHT/4*3)
WALL7 = wall(50, 50, 35, HEIGHT/4*3)
PT8 = platform(50, 50, WIDTH - 35, HEIGHT/4*3)
WALL8 = wall(50, 50, WIDTH - 35, HEIGHT/4*3)
PT9 = platform(50, HEIGHT/2, 435, HEIGHT/4+100)
WALL9 = wall(50, HEIGHT/2, 435, HEIGHT/4+100)
PT10 = platform(50, HEIGHT/2, WIDTH - 435, HEIGHT/4+100)
WALL10 = wall(50, HEIGHT/2, WIDTH - 435, HEIGHT/4+100)
PT11 = platform(50, 50, WIDTH/2-100, HEIGHT/4*3)
WALL11 = wall(50, 50, WIDTH/2-100, HEIGHT/4*3)
PT12 = platform(50, 50, WIDTH/2+100, HEIGHT/2)
WALL12 = wall(50, 50, WIDTH/2+100, HEIGHT/2)
PT13 = platform(50, 50, WIDTH/2-120, HEIGHT/4)
WALL13 = wall(50, 50, WIDTH/2-120, HEIGHT/4)
PT14 = platform(WIDTH/2, 50, WIDTH/4-165, 100)
WALL14 = wall(WIDTH/2, 50, WIDTH/4-165, 100)




P1 = Player1()
P2 = Player2()
obj = goal()

platforms = pygame.sprite.Group()
platforms.add(PT1)
platforms.add(PT2)
platforms.add(PT3)
platforms.add(PT4)
platforms.add(PT5)
platforms.add(PT6)
platforms.add(PT7)
platforms.add(PT8)
platforms.add(PT9)
platforms.add(PT10)
platforms.add(PT11)
platforms.add(PT12)
platforms.add(PT13)
platforms.add(PT14)

walls = pygame.sprite.Group()
walls.add(WALL1)
walls.add(WALL2)
walls.add(WALL3)
walls.add(WALL4)
walls.add(WALL5)
walls.add(WALL6)
walls.add(WALL7)
walls.add(WALL8)
walls.add(WALL9)
walls.add(WALL10)
walls.add(WALL11)
walls.add(WALL12)
walls.add(WALL13)
walls.add(WALL14)


all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(WALL1)
all_sprites.add(PT2)
all_sprites.add(WALL2)
all_sprites.add(PT3)
all_sprites.add(WALL3)
all_sprites.add(PT4)
all_sprites.add(WALL4)
all_sprites.add(PT5)
all_sprites.add(WALL5)
all_sprites.add(PT6)
all_sprites.add(WALL6)
all_sprites.add(PT7)
all_sprites.add(WALL7)
all_sprites.add(PT8)
all_sprites.add(WALL8)
all_sprites.add(PT9)
all_sprites.add(WALL9)
all_sprites.add(PT10)
all_sprites.add(WALL10)
all_sprites.add(PT11)
all_sprites.add(WALL11)
all_sprites.add(PT12)
all_sprites.add(WALL12)
all_sprites.add(PT13)
all_sprites.add(WALL13)
all_sprites.add(PT14)
all_sprites.add(WALL14)


all_sprites.add(P1)
all_sprites.add(P2)
all_sprites.add(obj)


completed = False
#while loop for game run
while True:

    P1.move1()
    P2.move2()
    P1.update1()
    P2.update2()
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit() #idk why this isnt recognized by python
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_UP:
                P1.jump1()
            if event.key == pygame.K_w:
                P2.jump2()
            
    displaysurface.blit(bg, (0, 0))
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
 
    colision(P1, P1com, P2com)
    pygame.display.update()
    FramePerSec.tick(FPS)
