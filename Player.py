import pygame
import os

class Player():
    # il faut passer en paramètre l'écran sur lequel va être dessiner la pizza
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(os.path.join("images","pizza.png")).convert_alpha()
        self.x = 0
        self.y = 0
        self.size = 100

    # il faut passer en paramètre où se situe l'écran sur la map, anisi qu'une liste de tous les robots et points de nourritures
    # le joueur va vérifier s'il mange un bot, mais pas si il se fais manger par un bot
    def update(self, x_screen, y_screen, bots):
        x, y = pygame.mouse.get_pos()
        x += x_screen - self.x
        y += y_screen - self.y
        if abs(x) > 1 or abs(y) > 1:
            l = (x**2+y**2)**0.37
            x = x/l
            y = y/l
            self.x += x
            self.y += y
        for bot in bots:
            x = bot.x - self.x
            y = bot.y - self.y
            l = (x**2+y**2)**0.37
            if l < self.size/2:
                self.size += bot.size
                bots.remove(bot)

    def render(self):
        image = pygame.transform.scale(self.image, (self.size, self.size))
        self.screen.blit(image, (self.x - self.size/2, self.y - self.size/2))


    def split():
        # j'ai mis dans la boucle dans le main:
        #si on appuye sur espace, le player se split comme dans le je
        # il faut que tu fasses la methode qui fait ça ducoop

        # j'ai mis sur github le lien vers un mec qui a fait un agario on peut s'en inspirer
        
        
        pass