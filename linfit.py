#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import yoshida

#call as yoshida modeno filename
modeno = int(sys.argv[1])
filename = sys.argv[2]

data = np.genfromtxt(filename)
maxnt = data.shape[0]

if len(sys.argv) > 3:
  maxnt = int(sys.argv[3])

t = data[:maxnt,0]
re = data[:maxnt,2*modeno-1]
im = data[:maxnt,2*modeno]
am = np.sqrt(re**2+im**2)

dt=t[1]-t[0]
(w,d,a,p) = yoshida.fyoshida(re,dt)

print 'frequency is ', w
print 'growth rate is ', d

