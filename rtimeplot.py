#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]

data = np.genfromtxt(filename)

t = data[:,0]
re = data[:,1]

plt.figure(1)
plt.plot(t,re)
plt.xlabel('$\Omega_i t$')
plt.savefig('rmodelin.png')

plt.figure(2)
plt.plot(t,abs(re))
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.savefig('rmodelog.png')

plt.show()
