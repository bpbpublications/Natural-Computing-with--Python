import matplotlib.pyplot as plt
import numpy as np

import cellpylib as cpl

# NKS page 442 - Rule 122R
cellular_automaton = np.array([[0]*40 + [1]*20 + [0]*40])
r = cpl.ReversibleRule(cellular_automaton[0], 122)
cellular_automaton = cpl.evolve(cellular_automaton,\
                                timesteps=1000,\
                                apply_rule=r.apply_rule)

timestep = []
average_cell_entropies = []

for i, c in enumerate(cellular_automaton):
    timestep.append(i)
    average_cell_entropies.append\
                                   (cpl.average_cell_entropy\
                                    (cellular_automaton[:i+1]))
    

plt.figure(1)
plt.title("Avg. Cell (Shannon) Entropy")
plt.plot(timestep, average_cell_entropies)

plt.figure(2)
plt.title("Rule 122R Cellular Automata")
cpl.plot(cellular_automaton)


