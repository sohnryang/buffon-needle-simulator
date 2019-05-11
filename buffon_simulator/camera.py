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
        Initialize self.
        """
        self.win = win
        self.zoom = zoom

    def world_projection(self):
        """
        Project the world.
        """
        gl.glDisable(gl.GL_DEPTH_TEST)
        gl.glViewport(0, 0, self.win.width, self.win.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        width_ratio = self.win.width / self.win.height
        gl.gluOrtho2D(
            -self.zoom * width_ratio,
            self.zoom * width_ratio,
            -self.zoom, self.zoom
        )
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
    
    def label_projection(self):
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.gluOrtho2D(0, self.win.width, 0, self.win.height)