import pygame
import time
from pygame.locals import *
from sys import exit
import random
from random import randint

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Dado') 

PRETO = (0,0,0)
barulho_colisao = pygame.mixer.Sound('Dados\MANYDICE.wav')
barulho_colisao.set_volume(0.2)

class Dado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load(r'C:\Users\JoaoVictor\OneDrive\Área de Trabalho\Monitoria\Dados\1_dot.png'))
        self.sprites.append(pygame.image.load(r'C:\Users\JoaoVictor\OneDrive\Área de Trabalho\Monitoria\Dados\2_dots.png'))
        self.sprites.append(pygame.image.load(r'C:\Users\JoaoVictor\OneDrive\Área de Trabalho\Monitoria\Dados\3_dots.png'))
        self.sprites.append(pygame.image.load(r'C:\Users\JoaoVictor\OneDrive\Área de Trabalho\Monitoria\Dados\4_dots.png'))
        self.sprites.append(pygame.image.load(r'C:\Users\JoaoVictor\OneDrive\Área de Trabalho\Monitoria\Dados\5_dots.png'))
        self.sprites.append(pygame.image.load(r'C:\Users\JoaoVictor\OneDrive\Área de Trabalho\Monitoria\Dados\6_dots.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False
        self.contador = 25
 
    
    
    def girar_dado(self):
        if self.animar == False:
            barulho_colisao.play()
            self.animar = True
      
     

    def update(self):
        
        if self.animar == True:
            if self.contador != 0:
                self.atual = randint(0,5)
                print(self.contador)
                self.contador-=1
            else:
                self.atual = randint(0,5)
                self.contador = 25
                self.animar = False
            self.image = self.sprites[self.atual]
        
       
         
            

todas_as_sprites = pygame.sprite.Group()
dado = Dado()
todas_as_sprites.add(dado)
        

relogio  = pygame.time.Clock()
while True:
    relogio.tick(30)

    tela.fill(PRETO)
    todas_as_sprites.draw(tela) #Desenhar na tela
    todas_as_sprites.update() #Faz o update
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            dado.girar_dado()
        
                   
            