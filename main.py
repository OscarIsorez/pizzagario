import pygame
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

def fonctions_player():
    cam.x = player.x - taille_fenetre[0]/2
    cam.y = player.y - taille_fenetre[1]/2
    grid.draw()
    for food in bots:
        food.render()
    player.render()
    player.update(bots)


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    pygame.display.set_caption('pizzagario')

    screen = pygame.display.set_mode(taille_fenetre)




    play_button_image = pygame.image.load(os.path.join("images","button.png"))
    play_button = pygame.transform.scale(play_button_image,(400, 180))
    play_button_rect =play_button.get_rect()
    play_button_rect.x = math.ceil( screen.get_width()/4)
    play_button_rect.y =  math.ceil( screen.get_height()/4)



    cam = Camera(1, 0, 0)
    player = Player(screen, cam)
    grid = Grid(screen, cam)

    bots = []
    for i in range(10):
        for j in range(10):
            bots.append(Food(screen, i*50, j*50, cam))

    is_playing = False

    def ecran_de_demarrage():
        global is_playing
        screen.fill((0,255,0))
        screen.blit(play_button, play_button_rect)

    RUNNING = True



    # grille  = Grid(screen, taille_fenetre)
    while RUNNING:
        time.sleep(0.01)
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


        if not is_playing:
            ecran_de_demarrage()
        else:
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 0, 1000, 1000))
            fonctions_player()



        pygame.display.flip()



