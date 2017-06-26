#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

#call as xplot.py ts filename
ts = int(sys.argv[1])
filename = sys.argv[2]

data = np.genfromtxt(filename)

nx = data.shape[1]-2
nt = data.shape[0]

t = data[:,0]
xdata = data[ts,1:nx+1]

plt.plot(range(nx),xdata)
plt.xlabel('$n_x$')
plt.show()
