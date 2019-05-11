"""
Class World
===========

A world (model) class used for pyglet rendering of visualizer.
"""
from buffon_simulator.grid import Grid
import pyglet.gl as gl


class World:
    """
    World(self)

    A world (or model) object.

    Parameters
    ----------

    win_size : (int, int)
        Size of the window.
    """
    def __init__(self, win_size):
        """
        Initalize self.
        """
        self.ents = {}
        self.next_entitiy_id = 0
        self.width = win_size[0]
        self.height = win_size[1]
        x = -self.width / self.height
        while x <= self.width / self.height:
            ent = Grid(self.next_entitiy_id, x)
            self.ents[ent.id] = ent
            self.next_entitiy_id += 1
            x += 0.2

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
