import numpy as np
import matplotlib.pyplot as plt 
import math

g = 9.81

class Projectile:
    def __init__(self,x0,y0,v0,theta,m,rho,C_d,A,dt=0.01):
        self.x = x0
        self.y = y0
        self.vx = v0 * math.cos(math.radians(theta))
        self.vy = v0 * math.sin(math.radians(theta))
        self.m = m
        self.rho = rho
        self.C_d = C_d
        self.A = A
        self.dt = dt

    def pomak(self):
        x_podaci = []
        y_podaci = []

        while self.y >= 0:
            self.ax = -np.sign(self.vx)*(self.rho*self.C_d*self.A/2*self.m)*self.vx**2
            self.ay = - g -np.sign(self.vy)*(self.rho*self.C_d*self.A/2*self.m)*self.vy**2
            self.vx += self.ax*self.dt
            self.vy += self.ay*self.dt
            self.x += self.vx*self.dt
            self.y += self.vy*self.dt

            x_podaci.append(self.x)
            y_podaci.append(self.y)

        return x_podaci, y_podaci
    
    def runge_kutta(self):
        x_podaci = []
        y_podaci = []

        while self.y >= 0:
            self.k1vx =  -np.sign(self.vx)*(self.rho*self.C_d*self.A/(2*self.m))*(self.vx)**2*self.dt
            self.k1vy = (-g -np.sign(self.vy)*(self.rho*self.C_d*self.A/(2*self.m))*(self.vy)**2)*self.dt
            self.k1x = self.vx*self.dt
            self.k1y = self.vy*self.dt
            self.k2vx = -np.sign(self.vx+self.k1vx/2)*(self.rho*self.C_d*self.A/(2*self.m))*(self.vx+self.k1vx/2)**2*self.dt
            self.k2vy = (-g -np.sign(self.vy+self.k1vy/2)*(self.rho*self.C_d*self.A/(2*self.m))*(self.vy+self.k1vy/2)**2)*self.dt
            self.k2x = (self.vx+self.k1vx/2)*self.dt
            self.k2y = (self.vy+self.k1vy/2)*self.dt
            self.k3vx = -np.sign(self.vx+self.k2vx/2)*(self.rho*self.C_d*self.A/(2*self.m))*(self.vx+self.k2vx/2)**2*self.dt
            self.k3vy = (-g -np.sign(self.vy+self.k2vy/2)*(self.rho*self.C_d*self.A/(2*self.m))*(self.vy+self.k2vy/2)**2)*self.dt
            self.k3x = (self.vx+self.k2vx/2)*self.dt
            self.k3y = (self.vy+self.k2vy/2)*self.dt
            self.k4vx = -np.sign(self.vx+self.k3vx/2)*(self.rho*self.C_d*self.A/(2*self.m))*(self.vx+self.k3vx/2)**2*self.dt
            self.k4vy = (-g -np.sign(self.vy+self.k3vy/2)*(self.rho*self.C_d*self.A/(2*self.m))*(self.vy+self.k3vy/2)**2)*self.dt
            self.k4x = (self.vx+self.k3vx/2)*self.dt
            self.k4y = (self.vy+self.k3vy/2)*self.dt
            self.vx += 1/6*(self.k1vx+2*self.k2vx+2*self.k3vx+2*self.k4vx)
            self.vy += 1/6*(self.k1vy+2*self.k2vy+2*self.k3vy+2*self.k4vy)
            self.x += 1/6*(self.k1x+2*self.k2x+2*self.k3x+2*self.k4x)
            self.y += 1/6*(self.k1y+2*self.k2y+2*self.k3y+2*self.k4y)

            x_podaci.append(self.x)
            y_podaci.append(self.y)

        return x_podaci, y_podaci
        
    def plot_trajectory(self):
        x,y = self.pomak()
        plt.plot(x,y)
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.title("x-y graf")
        plt.show()
