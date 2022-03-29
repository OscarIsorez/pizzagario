import pygame
# from Ennemi import Ennemies
from Player import Player
from Food import Food
from Camera import Camera
from Grid import Grid
import time
import sys
import math
import os
# from Grid import Grid
taille_fenetre = (640, 480)

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('pizzagario')
    screen = pygame.display.set_mode(taille_fenetre)

    x_play_button, y_play_button = 100,100
    #image bouton play
    play_button_image = pygame.image.load(os.path.join("images","jouer.png"))
    play_button = pygame.transform.scale(play_button_image,(x_play_button, y_play_button))
    play_button_rect =play_button.get_rect()
    play_button_rect.x = math.ceil( screen.get_width()/5.6)
    play_button_rect.y =  math.ceil( screen.get_height()/3)

    background_depart_image = pygame.image.load(os.path.join("images","menu_background.jpg"))
    background_depart = pygame.transform.scale(background_depart_image,taille_fenetre)
    background_depart_rect = background_depart.get_rect()


    ton_score =0
    score_inscrit = f'Score: {ton_score}'
    X = taille_fenetre[0]
    Y = taille_fenetre[1]
    green = (221, 120, 43)
    blue = (0, 0, 128)
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(score_inscrit, True, green)
    textRect = text.get_rect()
    textRect.center = (X-550 , Y-440)
    

    cam = Camera(1, 0, 0)
    player = Player(screen, cam)
    # ennemi = Ennemies(screen, cam)
    grid = Grid(screen, cam)
    boule = []
    
   
    is_playing = False

    def ecran_de_demarrage():
        global is_playing
        screen.blit(background_depart, background_depart_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(text, textRect)
    
        
    def fonctions_player():
        cam.x = player.x - taille_fenetre[0]/2
        cam.y = player.y - taille_fenetre[1]/2
        grid.draw()
        for food in boule:
            food.render()
        player.render()
        player.update(boule)

    # def fonctions_ennemi():
    #     ennemi.render()
    #     ennemi.update(boule)


    def ajout_boule_sur_grille():
            for i in range(50):
                for j in range(50):
                    boule.append(Food(screen, i*50, j*50, cam))
    ajout_boule_sur_grille()


    RUNNING = True



    while RUNNING:
        time.sleep(0.01)
        mouse = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    player.split(0, 0)  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    is_playing = True
            if event.type == pygame.MOUSEMOTION:
                if play_button_rect.collidepoint(event.pos):
                    play_button = pygame.transform.scale(play_button_image,(x_play_button +20, y_play_button+20))
                    
                else:
                    play_button = pygame.transform.scale(play_button_image,(x_play_button, y_play_button))


        if not is_playing:
            ecran_de_demarrage()
        else:
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 0, 1000, 1000))
            fonctions_player()
            # fonctions_ennemi()
            

        
        pygame.display.flip()


        
