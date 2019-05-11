"""
Class HUD
=========

A HUD that shows framerate and other information.
"""
from pyglet import clock, font
import pyglet.gl as gl


class HUD:
    """
    HUD(self)

    A HUD for framerate.
    """
    def __init__(self, win):
        """
        Initialize self.
        """
        self.fps = clock.ClockDisplay()

    def draw(self):
        """
        Draw the HUD.
        """
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        self.fps.draw()
