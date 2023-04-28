import calculus as cal
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*(x**2) + 3


gore = []
dolje = []
trapez = []

koraci = np.arange(100, 1000, 50) 

for i in koraci:
    gore.append(cal.integracija(f, 0, 1, i)[0])
    dolje.append(cal.integracija(f, 0, 1, i)[1])
    trapez.append(cal.trapezna_integracija(f, 0, 1, i))


plt.title("Numerical integration")
plt.xlabel("N steps")
plt.ylabel("Integral")
plt.hlines(y=11/3, xmin=100, xmax=1000)
plt.scatter(koraci, trapez, s=5)
plt.scatter(koraci, gore, s=5)
plt.scatter(koraci, dolje, s=5)
plt.ylim(3.645,3.690)
plt.xlim(0,1000)
plt.show()

