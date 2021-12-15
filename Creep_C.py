from pygame.math import Vector2
import core
import pygame
import random
import math


class Creep_C:
    def __init__(self):

        self.pos_C = Vector2(random.randint(0, 1500), random.randint(0, 800))
        self.couleur_C = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon_C = 3

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_C, self.pos_C, self.rayon_C)