#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import time

#call as xmovie.py filename skip

filename = sys.argv[1]
skip = int(sys.argv[2])

data = np.genfromtxt(filename)

nx = data.shape[1]-2
nt = data.shape[0]

t = data[:,0]
xdata = data[:,1:]
dt = t[1]-t[0]


f = plt.figure()
a = f.gca()
f.show()
for t in range(0,nt,skip):
  a.clear()
  a.plot(range(nx+1),xdata[t,:])
  f.suptitle('T = '+str(dt*t))
  f.canvas.draw()
  time.sleep(0.01)
  
