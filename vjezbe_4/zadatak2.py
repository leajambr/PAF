import particle as prt
import numpy as np
import matplotlib.pyplot as plt
import sympy

greska = []
vrijeme = []
t = 0

while t<= 0.1:

    t+=0.0001

    vrijeme.append(t)

    p1 = prt.Particle(10,60,0,0)

    polozaji = p1.položaj(t)    

    x = [p[0] for p in polozaji] 

    greska.append(100*(abs(p1.range()-x[-1])/p1.range()))


plt.plot(vrijeme, greska)
plt.figtext(0.16,0.8," (Err) = | D_analitical - D_numerical | / D_analitical * (100%) ")
plt.title("Absolute relative error for range of projectile")
plt.xlabel("dt[s]")
plt.ylabel("Absolute relative error [%]")
plt.show()

