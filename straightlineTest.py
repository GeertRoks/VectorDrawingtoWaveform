import numpy as np
import matplotlib.pyplot as plt
import math

fs = 48000
f = 440

t = np.arange(0., 1., f/fs)

def linearBezier(p0, p1, t):
    pFinal = np.zeros(2)
    pFinal[0] = (1-t) * p0[0] + t*p1[0]
    pFinal[1] = (1-t) * p0[1] + t*p1[1]

    return pFinal

x = np.zeros(math.floor(fs/f))

for ti in range(np.size(t)-1):
    x[ti] = linearBezier(np.array([-1,-1]), np.array([1,1]), ti)[0]


