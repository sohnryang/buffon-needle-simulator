"""
Simulatino Application
======================

This is a visualizer application for simulation.
"""
from pyglet import clock, window
from buffon_simulator.camera import Camera
from buffon_simulator.hud import HUD
from buffon_simulator.world import World


class App:
    """
    App(self, count)

    The application object.

    Parameters
    ----------
    count : int
        Number of needles to throw
    """
    def __init__(self, count):
        """
        Initalize self.
        """
        self.win = window.Window(fullscreen=True, vsync=True)
        self.world = World((self.win.width, self.win.height))
        self.camera = Camera(self.win, zoom=1.0)
        self.hud = HUD(self.win)
        self.count = count
        clock.set_fps_limit(60)

    def main_loop(self):
        """
        The main loop.
        """
        while not self.win.has_exit:
            self.win.dispatch_events()
            self.world.tick()
            self.camera.world_projection()
            self.world.draw()
            clock.tick()
            self.win.flip()
