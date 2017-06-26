#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

#call as smoothplot.py modeno filename sigma
modeno = int(sys.argv[1])
filename = sys.argv[2]
sigma = float(sys.argv[3])

data = np.genfromtxt(filename)

t = data[:,0]
re = scipy.ndimage.filters.gaussian_filter(data[:,2*modeno-1],sigma)
im = scipy.ndimage.filters.gaussian_filter(data[:,2*modeno],sigma)
am = np.sqrt(re**2+im**2)

plt.figure(1)
plt.plot(t,re,t,im,t,am)
plt.xlabel('$\Omega_i t$')
plt.legend(['Real','Imaginary','Amplitude'])
plt.savefig('lin'+str(modeno)+'.png')

plt.figure(2)
plt.plot(t,am)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.savefig('log'+str(modeno)+'.png')

plt.show()
