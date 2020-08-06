import cellpylib as cpl

cellular_automaton = cpl.init_simple(200)

cellular_automaton = cpl.evolve(cellular_automaton,\
                                timesteps=100,\
                                apply_rule=lambda n,\
                                c, t: cpl.nks_rule(n, 110))

cpl.plot(cellular_automaton)
