"""
Buffon's needle simulator
=========================

This simulates a needle dropped on some floor.
The value of pi can be estimated by running this simulation.

For more information about buffon's needle problem and pi value estimation,
see https://en.wikipedia.org/wiki/Buffon%27s_needle_problem.
"""


class Simulator:
    """
    Simulator(self, count=1000)

    A simulator object. The code in this simulator runs all the simulation
    needed.

    Parameters
    ----------
    count : int, optional
        Number of needle throw.
    """
    def __init__(self, count=1000):
        """
        Initialize self.
        """
        self.count = count

    def run_simulation(self):
        """
        Run simulation.
        """
