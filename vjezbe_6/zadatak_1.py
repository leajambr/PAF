import matplotlib.pyplot as plt
import oscilator as ho
import numpy as np

h1 = ho.HarmonicOscillator(0.3,10,10,1.0)  # x0 v0 k m
h1.plot_trajectory(0.01,10) #dt, tmax
