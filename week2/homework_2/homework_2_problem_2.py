# Jessica Schonhut-Stasik 
# Homework 2 - Problem 2
# Simple Harmonic Oscillator

# import modules 
import numpy as np 
import matplotlib.pyplot as plt
from homework_2 import forward
from homework_2 import central


time, pos = np.loadtxt('position_data.txt', delimiter=',', usecols=(0,1), unpack=True, skiprows=0)

plt.plot(time, pos)
plt.savefig('position_vs_time.png')
plt.clf()
 
vel_forward = forward(pos, 0.01)
plt.plot(time, vel_forward)

vel_central = central(pos, 0.01)
plt.plot(time, vel_central)
plt.savefig('velocity_vs_time_both.png')
plt.clf()

