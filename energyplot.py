# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

#call as timeplot.py modeno filename sigma

filename = 'energy.out'

data = np.genfromtxt(filename)

t = data[:,0]

fe = data[:,1]
ke = data[:,2]
te = data[:,3]


plt.figure(1)
plt.plot(t,fe,t,ke,t,te)
plt.xlabel('$\Omega_i t$')
plt.legend(['field energy', 'kinetic energy', 'total energy'],loc='best')
plt.savefig('lin'+str(modeno)+'.png')

plt.figure(2)
plt.plot(t,abs(fe),t,abs(ke),t,abs(te))
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.legend(['|field energy|', '|kinetic energy|', '|total energy|'],loc='best')
plt.savefig('log'+str(modeno)+'.png')


plt.show()
