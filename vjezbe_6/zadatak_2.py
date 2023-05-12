import matplotlib.pyplot as plt
import oscilator as ho
import numpy as np

h2 = ho.HarmonicOscillator(1.0,0.0,1.0,1.0)

fig,ax = plt.subplots()
lista_dt = [0.001,0.01,0.05]

for dt in lista_dt:
    T = 3*h2.period(dt)
    t, x_num = h2.oscillate(dt,T)   
    x_anal = h2.x_analitičko(t) 

    plt.plot(t,x_anal)
    plt.scatter(t,x_num)

plt.xlabel("t")
plt.ylabel("x")
plt.legend(["analitički","numerički"])
plt.show()


