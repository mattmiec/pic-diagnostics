#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

#call as timeplot.py modeno filename sigma
modeno = int(sys.argv[1])
filename = sys.argv[2]
if len(sys.argv)>3:
  sigma = int(sys.argv[3])
else:
  sigma = 0

data = np.genfromtxt(filename)

t = data[:,0]
if (sigma==0):
  re = data[:,2*modeno-1]
  im = data[:,2*modeno]
  am = np.sqrt(re**2+im**2)
else:
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
