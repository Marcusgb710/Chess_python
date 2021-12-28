import pygame

class piece():
    def __init__(self, x, y, r, color, name, pic=False):
        self.x = x
        self.y = y
        self.radius = r
        self.color = color
        self.name = name
        self.hasPic = pic