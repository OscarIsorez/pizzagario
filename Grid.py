

from Drawable import Drawable
import pygame

class Grid(Drawable):
    """classe pour faire la grille du jeu"""

    

    def __init__(self, surface, camera):
        super().__init__(surface, camera)
        self.color = (230,240,240)

    def draw(self):
        # A grid is a set of horizontal and prependicular lines
        zoom = self.camera.zoom
        x, y = self.camera.x, self.camera.y
        for i in range(0,2001,25):
            pygame.draw.line(self.surface,  self.color, (x, i*zoom + y), (2001*zoom + x, i*zoom + y), 3)
            pygame.draw.line(self.surface, self.color, (i*zoom + x, y), (i*zoom + x, 2001*zoom + y), 3)
