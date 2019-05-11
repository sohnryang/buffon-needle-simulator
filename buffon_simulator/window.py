"""
Simulation window
=================

A GUI window for visualizing simulation.
"""
import pyglet


class SimulationWindow(pyglet.window.Window):
    def __init__(self):
        """
        Initialize self.
        """
        super(SimulationWindow, self).__init__()
        self.width = 0
        self.height = 0

    def on_draw(self):
        self.clear()
        self.label.draw()

    def on_resize(self, width, height):
        self.width = width
        self.height = height
