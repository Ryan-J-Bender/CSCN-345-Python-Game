# CSCN 345 (003) Python Game by Isaac Scott and Ryan Bender
import pygame
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 600
WIDTH = 1250
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amish Boy and Amish Girl")

#class for player
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
    
    #colision update
    def update1(self):
        platforms = pygame.sprite.Group()
        platforms.add(PT1)

        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        if P1.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
                
    #movement function
    def move1(self):
        self.acc = vec(0,0.5)
 
        pressed_keys = pygame.key.get_pressed()
            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
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
    def jump1(self):
        platforms = pygame.sprite.Group()
        platforms.add(PT1)
        hits1 = pygame.sprite.spritecollide(self, platforms, False)
        if hits1:
            self.vel.y = -15
            
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255,50,40))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
    
    #colision update   
    def update2(self):
        platforms = pygame.sprite.Group()
        platforms.add(PT1)
        hits = pygame.sprite.spritecollide(P2 ,platforms, False)
        if P2.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
            
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
        platforms = pygame.sprite.Group()
        platforms.add(PT1)
        hits2 = pygame.sprite.spritecollide(self, platforms, False)
        if hits2:
            self.vel.y = -15
        
#class for platforms 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
        
PT1 = platform()
P1 = Player1()
P2 = Player2()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
all_sprites.add(P2)


#while loop for game run
while True:
    P1.move1()
    P2.move2()
    P1.update1()
    P2.update2()
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            #sys.exit() idk why this isnt recognized by python
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_UP:
                P1.jump1()
            if event.key == pygame.K_w:
                P2.jump2()
            
     
    displaysurface.fill((0,0,0))
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
 
    pygame.display.update()
    FramePerSec.tick(FPS)
