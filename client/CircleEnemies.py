import pygame
import os

class Circle():
    def __init__(self, x, y, size, vector_x, vector_y):
        self.x = x
        self.y = y
        self.vector_x = vector_x
        self.vector_y = vector_y
        self.size = size
        self.Player = Player

    def update(self, x, y, bots, player):
        self.time -= 1
        x -= self.x
        y -= self.y

        if abs(self.vector_x) != 0:
            self.vector_x = self.vector_x*127/128
            if abs(self.vector_x) < 0.1:
                self.vector_x = 0
        if abs(self.vector_y) != 0:
            self.vector_y = self.vector_y*127/128
            if abs(self.vector_y) < 0.1:
                self.vector_y = 0

        if abs(x) > 1 or abs(y) > 1:
            l = (x**2+y**2)**0.5
            x = x/l
            y = y/l
            self.x += x + self.vector_x
            self.y += y + self.vector_y