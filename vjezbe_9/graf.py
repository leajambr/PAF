import zadatak_1 as inter
import matplotlib.pyplot as plt
import numpy as np

masa_sunca = 1.989*10**30
masa_zemlje = 5.9742*10**24
r_sunca =  (0,0)
r_zemlje = (1.486*10**11,0)
v_zemlje = (0, 29783)
t = 365.242

zadatak = inter.interakcija(masa_sunca, masa_zemlje, r_sunca, r_zemlje, (0,0), v_zemlje)

putanje_sunca, putanje_zemlje = zadatak.euler(t)

plt.plot(putanje_sunca[:, 0], putanje_sunca[:, 1], "o",  label="Sunce", c = "y")
plt.plot(putanje_zemlje[:, 0],putanje_zemlje[:, 1], label = "Zemlja", c = "green")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Putanja Sunca i Zemlje")
plt.legend()
plt.show()