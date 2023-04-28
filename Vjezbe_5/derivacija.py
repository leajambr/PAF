import calculus as cal
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 5*x**3 - 2*x**2 + 2*x - 3

def df(x):
    return 5*3*x**2 - 2*2*x + 2

epsilon1 = cal.raspon_derivacije(f, -2, 2,0.1)
epsilon2 = cal.raspon_derivacije(f, -2, 2,0.01)

točke = np.arange(-2,2,0.01)
numerical_derivation = df(točke)

plt.title('Numerial derivation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(točke, numerical_derivation, color = 'red',label='Numeričko rješenje')
plt.scatter(epsilon1[0], epsilon1[1], label = '\u03B5 = 0.1', s=10)
plt.scatter(epsilon2[0], epsilon2[1], label = '\u03B5 = 0.01', s=5)
plt.legend()
plt.show()



