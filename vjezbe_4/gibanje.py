import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle(10,45,0,0)

print("Domet je {:.2f} m.".format(p1.range()))
p1.plot_trajectory()
p1.reset()