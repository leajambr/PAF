from zadatak_1 import nabijena_čestica
import matplotlib.pyplot as plt
import numpy as np


e = nabijena_čestica(q = -1, m = 1, E=(0,0,0), B =(0,0,1), v0 = (0.1,0.1,0.1), T0=(0,0,0))
p = nabijena_čestica(q = 1, m = 1, E=(0,0,0), B =(0,0,1), v0 = (0.1,0.1,0.1), T0=(0,0,0))

vrijeme = 10.00

e_putanja = e.gibanje(vrijeme)
p_putanja = p.gibanje(vrijeme)

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.plot(e_putanja[:,0],e_putanja[:,1],e_putanja[:,2], label="e")
ax.plot(p_putanja[:,0],p_putanja[:,1],p_putanja[:,2], label="p")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()
plt.show()
