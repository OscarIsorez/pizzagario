import pygame
import os
from CircleEnemies import Circle

class Enemy():
    # il faut passer en paramètre l'écran sur lequel va être dessiner la pizza
    def __init__(self, screen, cam):
        self.cam = cam
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()
        print(self.screen_width)
        self.image = pygame.image.load(os.path.join("images","pizza.png")).convert_alpha()
        self.circles = []
        self.circles.append(Circle(0, 0, 100, 0, 0))
        self.x = 0
        self.y = 0

    # il faut passer en paramètre où se situe l'écran sur la map, anisi qu'une liste de tous les robots et points de nourritures
    # le joueur va vérifier s'il mange un bot, mais pas si il se fais manger par un bot
    def update(self, bots):
        x, y = pygame.mouse.get_pos()
        x += self.x - self.screen_width/2
        y += self.y - self.screen_height/2
        self.x = 0
        self.y = 0

        for circle in self.circles:
            circle.update(x, y, bots, self)
            self.x += circle.x
            self.y += circle.y

        if len(self.circles) != 0:
            new_circles = []
            for circle in self.circles:
                for circle2 in self.circles:
                    if circle != circle2:
                        x = circle.x - circle2.x
                        y = circle.y - circle2.y
                        longueur = (x**2+y**2)**0.5
                        if longueur <circle.size/2 + circle2.size/2:
                            if longueur > 1 and (circle.time > 0 or circle2.time > 0):
                                circle.x += (x*(circle.size/2 + circle2.size/2 - longueur)/longueur)/2
                                circle.y += (y*(circle.size/2 + circle2.size/2 - longueur)/longueur)/2
                                circle2.x -= (x*(circle.size/2 + circle2.size/2 - longueur)/longueur)/2
                                circle2.y -= (y*(circle.size/2 + circle2.size/2 - longueur)/longueur)/2
                            if circle.time < 1 and circle2.time < 1 and (longueur <circle.size/2 or longueur <circle2.size/2):
                                new_circles.append(Circle((circle.x+circle2.x)/2, (circle.y+circle2.y)/2, circle.size + circle2.size, 0, 0))
                                self.circles.remove(circle)
                                self.circles.remove(circle2)
            self.circles += new_circles


            self.x = self.x / len(self.circles)
            self.y = self.y / len(self.circles)
            print(self.x)

    def render(self):
        for circle in self.circles:
            image = pygame.transform.scale(self.image, (circle.size, circle.size))
            self.screen.blit(image, (-image.get_width()/2 + self.screen_width/2 + circle.x - self.x, -image.get_height()/2 + self.screen_height/2  + circle.y - self.y))