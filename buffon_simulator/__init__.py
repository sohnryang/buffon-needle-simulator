"""__init__.py"""
import pyglet


def run_simulation(count):
    """run the simulation & bash the homework"""
    from buffon_simulator.simulator import Simulator
    sim = Simulator(count)
    sim.run_simulation()
    from buffon_simulator.window import Window
    win = Window()
    pyglet.app.run()
