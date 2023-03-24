import numpy as np
import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(F,m):

    a = F/m

    x = 0
    v = 0

    t = 0
    dt = 0.1

    x_podaci= []     
    t_podaci = []    
    v_podaci = []     
    a_podaci = []     


    while t<= 10:

        v = v + a*dt

        x = x + v*dt

        t = t + dt

        x_podaci.append(x)    
        t_podaci.append(t)
        v_podaci.append(v)
        a_podaci.append(a)

    plt.plot(t_podaci,a_podaci)
    plt.title("a-t graf")
    plt.xlabel("t[s]")
    plt.ylabel("a[m/s2]")
    plt.show()

    plt.plot(t_podaci,x_podaci)
    plt.title("x-t graf")
    plt.xlabel("t[s]")
    plt.ylabel("x[m]")
    plt.show()

    plt.plot(t_podaci,v_podaci)
    plt.title("v-t graf")
    plt.xlabel("t[s]")
    plt.ylabel("v[m/s]")
    plt.show()

jednoliko_gibanje(600,22)

def kosi_hitac(v0, theta,y):

    t = 0
    dt = 0.1
    x = 0
    g = - 9.81

    vy = v0*math.sin(math.radians(theta))   
    vx = v0*math.cos(math.radians(theta))

    x_podaci= []
    y_podaci = []
    t_podaci = []
    v_podaci = []

    while y >= 0.0:

        vy = vy + g*dt   
        vx = vx + 0*dt          # g = 0
        x = x + vx*dt
        y = y + vy*dt

        v = math.sqrt(vx**2 + vy**2)

        t = t + dt

        x_podaci.append(x)
        y_podaci.append(y)
        t_podaci.append(t)
        v_podaci.append(v)

    plt.plot(x_podaci,y_podaci)
    plt.title("x-y graf")
    plt.xlabel("x[m]")
    plt.ylabel("y[s]")
    plt.show()

    plt.plot(t_podaci,x_podaci)
    plt.title("x-t graf")
    plt.xlabel("t[s]")
    plt.ylabel("x[m]")
    plt.show()

    plt.plot(t_podaci,y_podaci)
    plt.title("y-t graf")
    plt.xlabel("t[s]")
    plt.ylabel("y[m]")
    plt.show()

kosi_hitac(10,45,2)
