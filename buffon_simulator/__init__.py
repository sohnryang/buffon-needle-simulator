"""__init__.py"""
import pyglet


def run_simulation(count):
    """run the simulation & bash the homework"""
    from buffon_simulator.app import App
    application = App(count, fullscreen=True, vsync=True)
    pyglet.app.run()