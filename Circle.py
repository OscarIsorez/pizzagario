import pygame
import os

class Circle():
    def __init__(self, x, y, size, vector_x, vector_y):
        self.x = x
        self.y = y
        self.vector_x = vector_x
        self.vector_y = vector_y
        self.size = size

    def update(self, x, y, bots):
        x += - self.x + self.vector_x
        y += - self.y + self.vector_y
        
        if abs(self.vector_x) != 0:
            self.vector_x = self.vector_x*63/64
            if abs(self.vector_x) < 1:
                self.vector_x = 0
        if abs(self.vector_y) != 0:
            self.vector_y = self.vector_y*63/64
            if abs(self.vector_y) < 1:
                self.vector_y = 0
        
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