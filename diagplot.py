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
w2 = data[:,2]

qx = scipy.ndimage.filters.gaussian_filter(qx,100)

plt.figure(1)
plt.plot(t,qx)
plt.xlabel('$\Omega_i t$')
plt.ylabel('$Q_x$')
plt.savefig('qflux.png')

plt.figure(2)
plt.plot(t,w2)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.ylabel('$<w^2>$')
plt.savefig('w2.png')


plt.show()
