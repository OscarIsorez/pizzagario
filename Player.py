import pygame

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
    
    def update(self):
        x, y = pygams