"""
Class World
===========

A world (model) class used for pyglet rendering of visualizer.
"""
from math import pi
from random import uniform
import pyglet.gl as gl
from buffon_simulator.grid import Grid
from buffon_simulator.needle import Needle


class World:
    """
    World(self)

    A world (or model) object.

    Parameters
    ----------

    win_size : (int, int)
        Size of the window.
    """
    def __init__(self, win_size, count):
        """
        Initalize self.
        """
        self.ents = {}
        self.next_entitiy_id = 0
        self.width = win_size[0]
        self.height = win_size[1]
        self.count = count
        x = -self.width / self.height
        while x <= self.width / self.height:
            ent = Grid(self.next_entitiy_id, x)
            self.ents[ent.id] = ent
            self.next_entitiy_id += 1
            x += 0.2
        for _ in range(count):
            x = uniform(-self.width / self.height, self.width / self.height)
            y = uniform(-1, 1)
            theta = uniform(0, pi)
            ent = Needle(self.next_entitiy_id, x, y, theta)
            self.ents[ent.id] = ent
            self.next_entitiy_id += 1

    def draw(self):
        """
        Draw the world.
        """
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glClearColor(255, 255, 255, 255)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        for ent in self.ents.values():
            ent.draw()

    def tick(self):
        """
        A tick of the clock in the world.
        """
