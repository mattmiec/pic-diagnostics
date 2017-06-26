#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]

data = np.genfromtxt(filename)

t = data[:,0]
re = data[:,1]
im = data[:,2]
am = np.sqrt(re**2+im**2)

plt.figure(1)
plt.plot(t,re,t,im,t,am)
plt.xlabel('$\Omega_i t$')
plt.legend(['Real','Imaginary'])
plt.savefig('cmodelin.png')

plt.figure(2)
plt.plot(t,am)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.savefig('cmodelog.png')

plt.show()
