import pygame
from Player import Player
import time
import sys
# from Grid import Grid
taille_fenetre = (640, 480)

def fonctions_player():
    player.render()
    player.update(0, 0, [])



if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    pygame.display.set_caption('pizzagario')

    screen = pygame.display.set_mode(taille_fenetre)
    
    player = Player(screen)

    # grille  = Grid(screen, taille_fenetre)
    while True:
        time.sleep(0.01)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.key == pygame.K_SPACE:
                player.split()
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 0, 1000, 1000))
        fonctions_player()
        
        
        pygame.display.flip()
        