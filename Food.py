import pygame
import os

class Food():
    def __init__(self, screen, x, y, cam):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = 1
        self.cam = cam

    def render(self):
        pygame.draw.circle(self.screen, (0, 255, 0),[self.x + int(self.cam.x), self.y + int(self.cam.y)], 10, 0)