#!/usr/bin/env python3
"""__main__.py"""
from sys import argv
import buffon_simulator

if len(argv) > 1:
    buffon_simulator.run_simulation(int(argv[1]))
else:
    buffon_simulator.run_simulation(1500)