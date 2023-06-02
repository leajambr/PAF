import numpy as np

class interakcija:
    def __init__(self,m1,m2,r1,r2,v1,v2,dt=1):   # 1 dan
        self.m1 = m1
        self.m2 = m2
        self.r1 = np.array(r1)
        self.r2 = np.array(r2)
        self.v1 = np.array(v1)
        self.v2 = np.array(v2)
        self.dt = dt*24*60*60     # dan u sekundama
        self.G = -6.67*10**(-11)

        self.lista_r1 = []
        self.lista_r2 = []

    def euler(self,t):
        t = t *24*60*60
        dts = np.arange(0, t, self.dt)
        for i in dts:
            
            a1 = ((self.G * self.m2) / (np.linalg.norm(self.r1 - self.r2))**3) * (self.r1 - self.r2)
            a2 = ((self.G * self.m1) / (np.linalg.norm(self.r2 - self.r1))**3) * (self.r2 - self.r1)
            
            self.v1 = self.v1 + a1 * self.dt
            self.v2 = self.v2 + a2 * self.dt
            self.r1 = self.r1 + self.v1 * self.dt
            self.r2 = self.r2 + self.v2 * self.dt

            self.lista_r1.append(self.r1)
            self.lista_r2.append(self.r2)   

        return np.array(self.lista_r1), np.array(self.lista_r2)


