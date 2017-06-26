#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

#call as timeplot.py filename1 filename2 newfilename
filename1 = sys.argv[1]
filename2 = sys.argv[2]
newfilename = sys.argv[3]

data1 = np.genfromtxt(filename1)
data2 = np.genfromtxt(filename2)

newdata = np.zeros(data1.shape)
newdata[:,0]=data1[:,0]
newdata[:,1::]=data1[:,1::]+data2[:,1::]

np.savetxt(newfilename,newdata)
