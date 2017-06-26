import numpy as np
import matplotlib.pyplot as plt

def fyoshida(x,dt):
#return [W, D, A, p]

  N = x.size
  nn = np.array(range(N))
  n2 = np.array(range(N/2))
  Xw = np.fft.fft(x)
  Xabs = np.amax(np.absolute(Xw[n2]))
  ind = np.argmax(np.absolute(Xw[n2]))
 
  #plot frequency spectrum
  plt.plot(2*np.pi*n2/dt/N,np.absolute(Xw[n2])**2)
  plt.yscale('log')
  plt.xlabel('$\omega$')
  plt.savefig('freq.png')

  #set four indices to be used
  k = np.array([ind-1, ind, ind+1])
  if (ind-2)>0:
    if abs(Xw[ind+2]) > abs(Xw[ind-2]):
      k = np.append(k,ind+2)
    else:
      k = np.insert(k,0,ind-2)
  else:
    k = np.append(k,ind+2)
  R = (Xw[k[0]]-2*Xw[k[1]]+Xw[k[2]])/(Xw[k[1]]-2*Xw[k[2]]+Xw[k[3]])
  #growth rate
  D = (2*np.pi)/N*(-3/(R-1)-1).imag
  #frequency
  if (k[3]-ind == 1):
    W = (2*np.pi/N)*(ind-3/(R-1)-2).real
  else:
    W = (2*np.pi/N)*(ind-3/(R-1)-1).real
  exarg = -1j*W*nn
  wsum = np.sum(np.exp(-1*D*nn))
  v = x*np.exp(exarg)
  A = 2*abs(np.sum(v)/wsum)
  p = -np.arctan(np.sum(v).imag/np.sum(v).real)

  W = W/dt
  D = -D/dt

  return (W,D,A,p)
