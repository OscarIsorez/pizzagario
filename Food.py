import pygame
import os

class Food():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = 1

    def render(self):
        pygame.draw.circle(self.screen, (0, 255, 0),[self.x, self.y], 10, 0)