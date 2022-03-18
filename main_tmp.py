import pygame
from Player import Player
from Food import Food
from Camera import Camera
from Grid import Grid
import time
import sys
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

    cam = Camera(1, 0, 0)
    player = Player(screen, cam)
    grid = Grid(screen, cam)

    bots = []
    for i in range(10):
        for j in range(10):
            bots.append(Food(screen, i*50, j*50, cam))


    # grille  = Grid(screen, taille_fenetre)
    while True:
        time.sleep(0.01)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.split(0, 0)
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 0, 1000, 1000))
        fonctions_player()


        pygame.display.flip()
