"""
Simulatino Application
======================

This is a visualizer application for simulation.
"""
from pyglet import clock
from pyglet.text import Label
from pyglet.window import Window
from buffon_simulator.camera import Camera
from buffon_simulator.world import World
import pyglet.gl as gl


class App(Window):
    """
    App(self, count)

    The application object.

    Parameters
    ----------
    count : int
        Number of needles to throw
    """
    def __init__(self, count, *args, **kwargs):
        """
        Initialize self.
        """
        super(App, self).__init__(*args, **kwargs)
        self.world = World((self.width, self.height), count)
        self.camera = Camera(self, zoom=1.0)
        self.count = count
        self.label = Label('', font_name='Meslo LG M', font_size=20,
                           x=10, y=self.height - 10,
                           anchor_x='left', anchor_y='top',
                           color=(0, 0, 0, 255))
        clock.set_fps_limit(60)

    def on_draw(self):
        """
        The main loop.
        """
        self.clear()
        self.camera.world_projection()
        self.world.draw()
        self.label.text = '%d out of %d thrown, π = %f' % (
            self.count - self.world.count,
            self.count,
            2 / (self.world.crossed / (self.count - self.world.count))
            if self.world.crossed > 0 else 0
        )
        self.camera.label_projection()
        self.label.draw()