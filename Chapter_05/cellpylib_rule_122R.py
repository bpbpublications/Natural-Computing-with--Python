import matplotlib.pyplot as plt
import numpy as np

import cellpylib as cpl

# NKS page 442 - Rule 122R
cellular_automaton = np.array([[0]*40 + [1]*20 + [0]*40])
r = cpl.ReversibleRule(cellular_automaton[0], 122)
cellular_automaton = cpl.evolve(cellular_automaton,\
                                timesteps=1000,\
                                apply_rule=r.apply_rule)

cpl.plot(cellular_automaton)


