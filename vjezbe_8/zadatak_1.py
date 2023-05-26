import numpy as np

class nabijena_čestica:
    def __init__(self,q,m,E,B,v0,T0,dt=0.01):
        self.q = q
        self.m = m
        self.E = np.array(E)
        self.B = np.array(B)
        self.v0 = np.array(v0)
        self.T0 = np.array(T0, dtype = np.float64)
        self.T = []
        self.dt = dt

    def gibanje(self,t):

        vrijeme = np.arange(0,t,self.dt)

        for t0 in vrijeme:

            a = (self.q/self.m)*(self.E+ (np.cross(self.v0, self.B)))
            self.v0 += a*self.dt
            self.T0 += self.v0*self.dt
            self.T.append(self.T0)

        return np.array(self.T)






