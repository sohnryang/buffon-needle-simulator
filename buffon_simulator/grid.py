"""
Class Grid
==========

A Grid class for drawing grids.
"""
import pyglet.gl as gl


class Grid:
    """
    Grid(self, id, x)

    A grid object.

    Parameters
    ----------
    id : int
        The grid's id as an entity.
    x : float
        The grid's x position.
    """
    def __init__(self, id, x):
        """
        Initalize self.
        """
        self.id = id
        self.x = x

    def draw(self):
        """
        Draws the grid.
        """
        gl.glLoadIdentity()
        gl.glTranslatef(self.x, -1, 0.0)
        gl.glLineWidth(1)
        gl.glBegin(gl.GL_LINES)
        gl.glColor4f(0, 0, 0, 255)
        gl.glVertex2f(0, 0)
        gl.glColor4f(0, 0, 0, 255)
        gl.glVertex2f(0, 2)
        gl.glEnd()
