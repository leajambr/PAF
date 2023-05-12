import math
import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self,x0,v0,k,m):
        self.x = x0
        self.v = v0
        self.k = k
        self.m = m
        self.a = -(self.k/self.m)*self.x
        self.t = 0.0

    def __move(self,dt):
        self.t += dt
        self.a =-(self.k/self.m)*self.x
        self.v += self.a*dt
        self.x += self.v*dt

    def plot_trajectory(self,dt,tmax):
        lista_t = []
        lista_x = []
        lista_v = []
        lista_a = []

        while self.t <= tmax:
            lista_t.append(self.t)
            lista_x.append(self.x)
            lista_v.append(self.v)
            lista_a.append(self.a)
            self.__move(dt)

        plt.plot(lista_t,lista_x)
        plt.title("x-t graf")
        plt.xlabel("t[s]")
        plt.ylabel("x[m]")
        plt.show()
        plt.plot(lista_t,lista_v)
        plt.title("v-t graf")
        plt.xlabel("t[s]")
        plt.ylabel("v[m/s]")
        plt.show()
        plt.plot(lista_t,lista_a)
        plt.title("a-t graf")
        plt.xlabel("t[s]")
        plt.ylabel("a[m/s^2]")
        plt.show()

    def period(self,dt):
        omega = math.sqrt(self.k/self.m)
        return 2*math.pi/omega
    
    def oscillate(self,dt,T):
        t = 0.0
        x_num = []

        while t<=T:
            x_num.append(self.x)
            self.__move(dt)
            t += dt
        return  np.linspace(0,T,len(x_num)),x_num
    
    def x_analitičko(self,t):
        omega = math.sqrt(self.k/self.m)
        return self.x*np.cos(omega*t)
    
    def plot(self,dt,T):
        t,x_num = self.oscillate(dt,T)
        x_anal = self.x_analitičko(t)
        plt.plot(t,x_anal)
        plt.scatter(t,x_num)
        plt.xlabel("t")
        plt.ylabel("x")
        plt.show()








    
        
     