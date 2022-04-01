import os
from Circle import Circle

class Player():
    # il faut passer en paramètre l'écran sur lequel va être dessiner la pizza
    def __init__(self):
        self.circles = []
        self.circles.append(Circle(0, 0, 100, 0, 0, 0))
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0

    # il faut passer en paramètre vers où doit aller la pizza
    def setTarget(x, y):
        self.target_x = x
        self.target_y = y

    # il faut passer en paramètre où se situe l'écran sur la map, anisi qu'une liste de tous les robots et points de nourritures
    # le joueur va vérifier s'il mange un bot, mais pas si il se fais manger par un bot
    def update(self, bots):
        x, y = self.target_x, self.target_y
        self.x = 0
        self.y = 0
        for circle in self.circles:
            circle.update(x, y, bots)
            self.x += circle.x
            self.y += circle.y

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
                            new_circles.append(Circle((circle.x+circle2.x)/2, (circle.y+circle2.y)/2, circle.size + circle2.size, 0, 0, 0))
                            self.circles.remove(circle)
                            self.circles.remove(circle2)
        self.circles += new_circles


        self.x = self.x / len(self.circles)
        self.y = self.y / len(self.circles)
        print(self.x)

    def split(self, x_screen, y_screen):
        old_circles = self.circles
        self.circles = []
        for circle in old_circles:
            if circle.size > 64:
                x = circle.x
                y = circle.y
                size = circle.size
                self.circles.append(Circle(x, y, circle.size//2, 0, 0, 1500))

                x_mouse, y_mouse = pygame.mouse.get_pos()
                x_mouse += x_screen - x
                y_mouse += y_screen - y

                l = (x_mouse**2+y_mouse**2)**0.5
                x_mouse = x_mouse/l
                y_mouse = y_mouse/l

                self.circles.append(Circle(x, y, circle.size//2, x_mouse*2, y_mouse*2, 1500))
            else:
                self.circles.append(circle)

