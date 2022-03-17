import pygame
import os
from Circle import Circle

class Player():
    # il faut passer en paramètre l'écran sur lequel va être dessiner la pizza
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(os.path.join("images","pizza.png")).convert_alpha()
        self.circles = []
        self.circles.append(Circle(0, 0, 100, 0, 0))
        self.x = 0
        self.y = 0

    # il faut passer en paramètre où se situe l'écran sur la map, anisi qu'une liste de tous les robots et points de nourritures
    # le joueur va vérifier s'il mange un bot, mais pas si il se fais manger par un bot
    def update(self, x_screen, y_screen, bots):
        x, y = pygame.mouse.get_pos()
        x += x_screen
        y += y_screen
        self.x = 0
        self.y = 0
        for circle in self.circles:
            circle.update(x, y, bots)
            self.x += circle.x
            self.y += circle.y
        self.x = self.x / len(self.circles)
        self.y = self.y / len(self.circles)

    def render(self):
        for circle in self.circles:
            image = pygame.transform.scale(self.image, (circle.size, circle.size))
            self.screen.blit(image, (circle.x - circle.size/2, circle.y - circle.size/2))


    def split():
        # j'ai mis dans la boucle dans le main:
        #si on appuye sur espace, le player se split comme dans le je
        # il faut que tu fasses la methode qui fait ça ducoop

        # j'ai mis sur github le lien vers un mec qui a fait un agario on peut s'en inspirer
        old_circle = self.circle
        self.circle = []
        for circle in old_circle:
            if circle.size > 64:
                x = circle.x
                y = circle.y
                size = circle.size
                self.circle.append(Circle(x, y, circle.size/2, 0, 0))
                
                x, y = pygame.mouse.get_pos()
                x += x_screen
                y += y_screen
                
                x += - self.x + self.vector_x
                y += - self.y + self.vector_y
                
                l = (x**2+y**2)**0.37
                x = x/l
                y = y/l
                self.x += x
                self.y += y
