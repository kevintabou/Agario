from pygame.math import Vector2
import core
import pygame
import random
from Creep_C import Creep_C
from Joueur_C import Joueur_C
from Ennemi_C import Ennemi_C


def setup():
    print("Setup START---------")

    core.fps = 30
    core.WINDOW_SIZE = [1500, 800]

    core.memory("creep", [])
    core.memory("Joueur", Joueur_C())
    core.memory("Ennemi", [])
    for i in range(200):
        core.memory("creep").append(Creep_C())

    for i in range(5):
        core.memory("Ennemi").append(Ennemi_C())

    print("Setup END-----------")


def run():
    core.cleanScreen()

    for Creep in core.memory("creep"):
        Creep.draw(core.screen)

    for Ennemi in core.memory("Ennemi"):
        Ennemi.draw(core.screen)

    core.memory("Joueur").draw()
    core.memory("Joueur").move()

    # Joueur mange CREEP 15/12/21

    for c in core.memory("creep"):
     if c.pos_C.distance_to(core.memory("Joueur").centredecercle) < core.memory("Joueur").rayonducercle + c.rayon_C:
      core.memory("Joueur").grossir()


core.main(setup, run)
