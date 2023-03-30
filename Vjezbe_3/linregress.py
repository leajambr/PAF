import matplotlib.pyplot as plt
import numpy as np
import math

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336]) # Nm              
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]) # rad     

                               # M = Dt * phi

                               # y = a*x + b , b = 0    

                               # a = mean xy / mean x**2

Dt = np.mean(phi*M)/ np.mean(phi**2)

print(Dt)

reg = Dt*phi

sigma_Dt = math.sqrt((np.mean(M**2)/np.mean(phi**2)-Dt**2)/len(M))  


plt.scatter(phi,M)
plt.figtext(0.32,0.8, "y = " + "{:.2f}".format(Dt)+"x")  # ubaci Dt i zaokr dvije decimale
plt.plot(phi,reg , color = "red" )
plt.xlabel("\u03C6 [rad]")
plt.ylabel("M [Nm]")
plt.legend(["data", "fit"], loc = "upper left")
plt.show()
print(sigma_Dt)

