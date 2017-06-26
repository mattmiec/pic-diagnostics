#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

#call as timeplot.py modeno filename sigma maxtstep
modeno = int(sys.argv[1])
filename = sys.argv[2]
sigma = int(sys.argv[3])
data = np.genfromtxt(filename)
if len(sys.argv)>4:
  maxts = int(sys.argv[4])
else:
  maxts = data.shape[0]

t = data[:maxts-1,0]
re = data[:maxts-1,2*modeno-1]
im = data[:maxts-1,2*modeno]
am = np.sqrt(re**2+im**2)
if (sigma!=0):
  re = scipy.ndimage.filters.gaussian_filter1d(re,sigma)
  im = scipy.ndimage.filters.gaussian_filter1d(im,sigma)
  am = np.sqrt(re**2+im**2)

imax = np.argmax(am)
tcrop = t[imax:]
amcrop = am[imax:]
[satamp] = np.polyfit(tcrop,amcrop,0)
fitline = np.linspace(satamp,satamp,tcrop.size)

print satamp

plt.figure(1)
plt.plot(t,re,t,im,t,am,tcrop,fitline)
plt.xlabel('$\Omega_i t$')
plt.legend(['Real','Imaginary','Amplitude','Saturated Fit'],loc=0)
plt.savefig('lin'+str(modeno)+'.png')

plt.figure(2)
plt.plot(t,am)
plt.yscale('log')
plt.xlabel('$\Omega_i t$')
plt.savefig('log'+str(modeno)+'.png')


plt.show()
