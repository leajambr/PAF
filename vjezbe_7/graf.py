import Projectile as project
import matplotlib.pyplot as plt

p1 = project.Projectile(0,0,20,45,5,0.5,0.1,0.02,0.1)
x1, y1 = p1.pomak()

p2 = project.Projectile(0,0,20,45,5,0.5,0.1,0.02,0.01)
x2, y2 = p2.pomak()

p3 = project.Projectile(0,0,20,45,5,0.5,0.1,0.02,0.001)
x3, y3 = p3.pomak()

p4 = project.Projectile(0,0,20,45,5,0.5,0.1,0.02,0.01)
x4, y4 = p4.runge_kutta()

plt.plot(x1,y1, label ="dt = 0.1, Euler")
plt.plot(x2,y2, label ="dt = 0.01, Euler")
plt.plot(x3,y3, label ="dt = 0.001, Euler")
plt.plot(x4,y4, label ="dt = 0.01, Runge-Kutta")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.title("x-y graf")
legenda = plt.legend(loc = "upper right")
plt.show()