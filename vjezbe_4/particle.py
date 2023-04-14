import math
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0,y0):  
        self.v0 = v0
        self.theta = theta
        self.x0 = x0                                
        self.y0 = y0  
        self.x = x0
        self.y = y0                                 
        self.vx = v0*math.cos(math.radians(theta))  
        self.vy = v0*math.sin(math.radians(theta))  

    def reset(self):   # sve staviti na 0
        self.v0 = 0
        self.theta = 0
        self.x0 = 0
        self.y0 = 0
        self.vx = 0
        self.vy = 0

    def __move(self,dt):   

        g = -9.81

        self.y += self.vy*dt
        self.vy += g*dt          
        self.x += self.vx*dt

    def položaj(self,dt):   # numeričko 

        Položaj = []

        while self.y >= 0:

            self.__move(dt)

            Položaj.append((self.x, self.y))

        return Položaj

    def range(self):   # analitičko
        
        max_Domet = (2*(self.v0)**2 * math.cos(math.radians(self.theta)) * math.sin(math.radians(self.theta)))/9.81

        return max_Domet

    def plot_trajectory(self):
     
     polozaji = self.položaj(0.01)    # dt = 0.01

     x = [p[0] for p in polozaji]   
     y = [p[1] for p in polozaji]  

     print(polozaji)

     plt.plot(x,y)
     plt.title("x-y graf")
     plt.xlabel("x")
     plt.ylabel("y")
     plt.show()


