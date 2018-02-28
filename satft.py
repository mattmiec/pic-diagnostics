# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:05:20 2018

@author: mtmiec
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

filename = 'phist.out'
modeno = 1
start = 40000
end = 100000

data = np.genfromtxt(filename)
t = data[start:end,0]
re = data[start:end,2*modeno-1]
im = data[start:end:,2*modeno]
am = np.sqrt(re**2+im**2)

dt = t[1] - t[0]
N = t.size
n2 = np.array(range(N))
ftre = np.fft.fft(im)
omega = 2*np.pi*n2/dt/N

plt.figure(1)
plt.plot(t,re,t,im,t,am)
plt.xlabel('$\Omega_i t$')
plt.legend(['Real','Imaginary','Amplitude'],loc=3)
plt.show()

#plot frequency spectrum
plt.figure(2)

plt.plot(2*np.pi*n2/dt/N,np.absolute(ftre[n2])**2)
plt.yscale('log')
plt.xlabel('$\omega$')
plt.show()