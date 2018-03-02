#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

#call as diagplot.py filename
filename = sys.argv[1]

data = np.genfromtxt(filename)

t = data[:,0]
qx = data[:,1]
w2i = data[:,2]
w2e = data[:,3]
kei = data[:,4]
kee = data[:,5]
fe = data[:,6]
te = data[:,7]

qx = scipy.ndimage.filters.gaussian_filter(qx,100)

plt.figure(1)
plt.plot(t,qx)
plt.xlabel('$\Omega_i t$')
plt.ylabel('$Q_x$')
plt.savefig('qflux.png')

plt.figure(2)
plt.plot(t,w2i)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.ylabel('$<w_i^2>$')
plt.savefig('w2i.png')

plt.figure(3)
plt.plot(t,w2e)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.ylabel('$<w_e^2>$')
plt.savefig('w2e.png')

plt.figure(4)
plt.plot(t,kei)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.ylabel('Ion Kinetic Energy')
plt.savefig('kei.png')

plt.figure(5)
plt.plot(t,kee)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.ylabel('Electron Kinetic Energy')
plt.savefig('kee.png')

plt.figure(6)
plt.plot(t,fe)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.ylabel('Field Energy')
plt.savefig('fe.png')

plt.figure(7)
plt.plot(t,te)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.ylabel('Total Energy')
plt.savefig('te.png')

plt.show()
