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
        meslo = font.load('Noto Sans', 10)
        self.text = font.Text(
            meslo,
            'Hello, world!',
            x=win.width / 2,
            y=win.width / 2,
            halign=font.Text.CENTER,
            valign=font.Text.CENTER,
            color=(0, 0, 0, 255)
        )

    def draw(self):
        """
        Draw the HUD.
        """
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        self.text.draw()
        self.fps.draw()
