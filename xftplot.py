#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

#call as xftplot.py kx filename
kx = int(sys.argv[1])
filename = sys.argv[2]

data = np.genfromtxt(filename)

nx = data.shape[1]-2
nt = data.shape[0]

t = data[:,0]
xdata = data[:,1:]

fkxr = np.zeros(nt)
fkxi = np.zeros(nt)
fkxa = np.zeros(nt)

for i in range(nt):
  ft = np.fft.fft(xdata[i,0:(nx-1)])
  fkxr[i] = ft[kx].real/nx
  fkxi[i] = ft[kx].imag/nx
  fkxa[i] = np.sqrt(fkxr[i]**2+fkxi[i]**2)

plt.plot(t,fkxr,t,fkxi,t,fkxa)
plt.xlabel('$\Omega_i t$')
plt.legend(['Real','Imaginary','Amplitude'])
plt.show()
