"""
Class Camera
============

A camera class for visualizer.
"""
import pyglet.gl as gl


class Camera:
    """
    Camera(self, win, zoom=1.0)

    A camera object.

    Parameters
    ----------
    win : pyglet.window.Window
        The pyglet window to use.
    zoom : float, optional
        The zoom value. Default is 1.0.
    """
    def __init__(self, win, zoom=1.0):
        """
        Initalize self.
        """
        self.win = win
        self.zoom = zoom

    def world_projection(self):
        """
        Project the world.
        """
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        width_ratio = self.win.width / self.win.height
        gl.gluOrtho2D(
            -self.zoom * width_ratio,
            self.zoom * width_ratio,
            -self.zoom, self.zoom
        )

    def hud_projection(self):
        """
        Project the HUD.
        """
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.gluOrtho2D(0, self.win.width, 0, self.win.height)
