"""
Class Needle
============

A class that represents a needle in simulation
"""
from math import sin, cos, ceil, floor
import pyglet.gl as gl


class Needle:
    """
    Needle(self, id, x, y, theta)

    A needle object.

    Parameters
    ----------
    id : int
        The needle's id as an entity.
    x : float
        The needle's x posotion.
    y : float
        The needle's y position.
    theta : float
        The needle's rotation.
    """
    def __init__(self, id, x, y, theta):
        """
        Initialize self.
        """
        self.id = id
        self.x = x
        self.y = y
        self.theta = theta

    def cross_check(self, x, theta):
        """
        Check if the needle is crossing the grid.

        Parameters
        ----------
        x : float
            The x coordinate of the needle.
        theta : float
            The needle's rotation.
        """
        x_min = min(x, x + cos(theta) * 0.2)
        x_max = max(x, x + cos(theta) * 0.2)
        x_min *= 5
        x_max *= 5
        return ceil(x_min) == floor(x_max)

    def draw(self):
        """
        Draw the needle.
        """
        gl.glLoadIdentity()
        gl.glTranslatef(self.x, self.y, 0.0)
        if self.cross_check(self.x, self.theta):
            gl.glColor4f(255, 0, 0, 255)
            gl.glLineWidth(3)
        else:
            gl.glColor4f(0, 0, 0, 255)
            gl.glLineWidth(1)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex2f(0, 0)
        gl.glVertex2f(cos(self.theta) * 0.2, sin(self.theta) * 0.2)
        gl.glEnd()
